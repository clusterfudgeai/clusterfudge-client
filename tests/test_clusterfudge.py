import clusterfudge
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
    assert result.queueing_behaviour.queue_launch == False

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
    assert result.queueing_behaviour.queue_launch == False

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

def test_all_gpus_are_available_and_properly_mapped():
    # First assertion is that the number of gpu fields on our Resources class
    # is the same as the number of gpu fields on the Resources proto.
    num_proto_gpu_fields = sum(1 for field in resources_pb2.Resources().DESCRIPTOR.fields if field.name.startswith('gpu_'))
    num_gpu_fields = len(vars(clusterfudge.Resources())) - 2 # cpus and memory_mb are not gpus
    assert num_proto_gpu_fields == num_gpu_fields

    # Then we create a launch requesting a unique value of each resource so we 
    # can assert each is correctly mapped.
    resources = clusterfudge.Resources()

    i = 1
    for attr, val in vars(resources).items():
        if isinstance(val, int):
            setattr(resources, attr, i)
            i+1

    client = clusterfudge.Client(api_key="skip_loading_config_file")
    client.launches_stub = MockLaunchesStub()

    clr = clusterfudge.CreateLaunchRequest(
        name="launch_with_lots_of_resources",
        jobs=[
            clusterfudge.Job(
                short_name="python",
                replicas=1,
                processes=[
                    clusterfudge.Process(
                        command=[""],
                        resource_requirements=resources,
                    ),
                ],
            ),
        ],
    )

    client.create_launch(clr)
    result = client.launches_stub.latest_launch.jobs[0].processes[0].resource_requirements
    
    for field in result.DESCRIPTOR.fields:
        if field.type == field.TYPE_INT32:
            actual_value = getattr(result, field.name)
            exp_value = getattr(resources, field.name.replace('gpu_', ''))
            assert actual_value == exp_value, f"Expected {field.name} to be {exp_value}, got {actual_value}"


def test_launch_with_queueing_behaviour():
    client = clusterfudge.Client(api_key="skip_loading_config_file")
    client.launches_stub = MockLaunchesStub()

    clr = clusterfudge.CreateLaunchRequest(
        name="launch_with_queueing_behaviour",
        description="unit test",
        queueing_behaviour=clusterfudge.QueueingBehaviour(
            enqueue_if_cluster_busy=True,
        ),
        jobs=[
            clusterfudge.Job(
                short_name="python",
                replicas=3,
                processes=[
                    clusterfudge.Process(
                        command=["python3", "app.py"],
                    ),
                ],
            ),
        ],
    )

    client.create_launch(clr)

    result = client.launches_stub.latest_launch 

    assert result.queueing_behaviour.queue_launch == True

class MockLaunchesStub:

    def CreateLaunch(self, request, metadata=None, timeout=None):
        self.latest_launch = request
        return launches_pb2.Launch()