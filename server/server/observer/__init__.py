from typing import Callable

from oremda.pipeline import Pipeline, OperatorNode, PipelineObserver

from ..messages import (
    pipeline_started,
    pipeline_completed,
    operator_started,
    operator_completed,
    NotificationMessage,
)


class ServerPipelineObserver(PipelineObserver):
    def __init__(self, notify: Callable[[NotificationMessage], None]):
        self.notify = notify

    def on_start(self, pipeline: Pipeline):
        message = pipeline_started({"id": pipeline.id})
        self.notify(message)

    def on_complete(self, pipeline: Pipeline):
        message = pipeline_completed({"id": pipeline.id})
        self.notify(message)

    def on_operator_start(self, pipeline: Pipeline, operator: OperatorNode):
        message = operator_started(
            {"pipelineId": pipeline.id, "operatorId": operator.id}
        )
        self.notify(message)

    def on_operator_complete(self, pipeline: Pipeline, operator: OperatorNode):
        message = operator_completed(
            {"pipelineId": pipeline.id, "operatorId": operator.id}
        )
        self.notify(message)
