import clusterfudge
from clusterfudge.clusterfudge import _proto_req_from_create_launch_request_v2
from clusterfudge_proto.launches import launches_pb2
from clusterfudge_proto.resources import resources_pb2
import pytest

def test_launch_with_git_branch():
    client = clusterfudge.Client(api_key="skip_loading_config_file")
    client.launches_stub = MockLaunchesStub()

    clr = clusterfudge.CreateLaunchRequest(
        name="launch_with_git_branch",
        description="unit test",
        deployment=clusterfudge.GitRepo(
            repo="https://github.com/clusterfudgeai/examples.git",
            branch="main",
        ),
        jobs=[
            clusterfudge.Job(
                short_name="python",
                replicas=3,
                replica_failure_behaviour=clusterfudge.OnReplicaFailureOtherReplicasAreStopped(),
                processes=[
                    clusterfudge.Process(
                        command=["python3", "app.py"],
                    ),
                    clusterfudge.Process(
                        command=["python3", "monitor.py"],
                        resource_requirements=clusterfudge.Resources(
                            rtx3090=1,
                        )
                    ),
                ],
            ),
        ],
    )

    client.create_launch(clr)

    result = client.launches_stub.latest_launch 

    assert result.title == clr.name
    assert result.description == clr.description
    assert result.cluster == ""
    assert result.shard == ""
    assert result.hostnames == []
    assert result.launch_script_body.startswith("import clusterfudge") # This is the first line of this test file
    assert result.jobs[0].short_name == clr.jobs[0].short_name
    assert result.jobs[0].replicas == clr.jobs[0].replicas
    assert result.jobs[0].on_replica_failure_other_replicas_are_stopped == launches_pb2.OnReplicaFailureOtherReplicasAreStopped()
    assert result.jobs[0].processes[0].command == clr.jobs[0].processes[0].command
    assert result.jobs[0].processes[1].command == clr.jobs[0].processes[1].command
    assert result.jobs[0].processes[0].resource_requirements == resources_pb2.Resources()
    assert result.jobs[0].processes[1].resource_requirements == resources_pb2.Resources(gpu_rtx3090=1)
    assert result.git_repo == clr.deployment.repo
    assert result.git_branch == clr.deployment.branch
    assert result.git_commit == ""


def test_launch_with_git_commit():
    client = clusterfudge.Client(api_key="skip_loading_config_file")
    client.launches_stub = MockLaunchesStub()

    clr = clusterfudge.CreateLaunchRequest(
        name="launch_with_git_commit",
        description="unit test",
        deployment=clusterfudge.GitRepo(
            repo="https://github.com/clusterfudgeai/examples.git",
            branch="main",
            commit="abcd123",
        ),
        jobs=[
            clusterfudge.Job(
                short_name="python",
                replicas=3,
                replica_failure_behaviour=clusterfudge.OnReplicaFailureOtherReplicasAreStopped(),
                processes=[
                    clusterfudge.Process(
                        command=["python3", "app.py"],
                    ),
                    clusterfudge.Process(
                        command=["python3", "monitor.py"],
                        resource_requirements=clusterfudge.Resources(
                            rtx3090=1,
                        )
                    ),
                ],
            ),
        ],
    )

    client.create_launch(clr)

    result = client.launches_stub.latest_launch 

    assert result.title == clr.name
    assert result.description == clr.description
    assert result.cluster == ""
    assert result.shard == ""
    assert result.hostnames == []
    assert result.launch_script_body.startswith("import clusterfudge") # This is the first line of this test file
    assert result.jobs[0].short_name == clr.jobs[0].short_name
    assert result.jobs[0].replicas == clr.jobs[0].replicas
    assert result.jobs[0].on_replica_failure_other_replicas_are_stopped == launches_pb2.OnReplicaFailureOtherReplicasAreStopped()
    assert result.jobs[0].processes[0].command == clr.jobs[0].processes[0].command
    assert result.jobs[0].processes[1].command == clr.jobs[0].processes[1].command
    assert result.jobs[0].processes[0].resource_requirements == resources_pb2.Resources()
    assert result.jobs[0].processes[1].resource_requirements == resources_pb2.Resources(gpu_rtx3090=1)
    assert result.git_repo == clr.deployment.repo
    assert result.git_branch == clr.deployment.branch
    assert result.git_commit == clr.deployment.commit


def test_launch_with_invalid_deployment_throws_error():
    client = clusterfudge.Client(api_key="skip_loading_config_file")
    client.launches_stub = MockLaunchesStub()

    launch_with_invalid_deployment = clusterfudge.CreateLaunchRequest(
        name="launch_with_invalid_deployment",
        description="unit test",
        deployment=clusterfudge.Resources(),
        jobs=[],
    )
    
    with pytest.raises(ValueError):
        client.create_launch(launch_with_invalid_deployment)


def test_launch_without_jobs_throws_error():
    client = clusterfudge.Client(api_key="skip_loading_config_file")
    client.launches_stub = MockLaunchesStub()

    launch_with_invalid_deployment = clusterfudge.CreateLaunchRequest(
        name="launch_with_invalid_deployment",
        description="unit test",
        deployment=clusterfudge.GitRepo(
            repo="https://github.com/clusterfudgeai/examples.git",
            branch="main",
        ),
        jobs=[],
    )
    
    try:
        client.create_launch(launch_with_invalid_deployment)
        assert False, "empty jobs array should have thrown an exception"
    except ValueError as e:
        assert str(e) == "jobs must be non-empty"


class MockLaunchesStub:

    def CreateLaunch(self, request, metadata=None, timeout=None):
        self.latest_launch = request
        return launches_pb2.Launch()