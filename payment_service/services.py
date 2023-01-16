import schemas
import uuid
from jaeger_client import Tracer
from opentracing_instrumentation.request_context import get_current_span, span_in_context
import opentracing


async def buy_sub(payment_info: schemas.BuySub) -> str:
    tracer = opentracing.global_tracer()
    with tracer.start_span(buy_sub.__name__, child_of=get_current_span()) as span:
        with span_in_context(span):
            sub_type = payment_info.sub_type
            qiwi = payment_info.qiwi
            uuid = payment_info.uuid
            #TODO some pay logic
            #TODO rabbitMQ to user make role
            return "success"
