import schemas
import uuid
from jaeger_client import Tracer
from opentracing_instrumentation.request_context import get_current_span, span_in_context
import opentracing
from broker import producer


async def buy_sub(payment_info: schemas.BuySub) -> str:
    tracer = opentracing.global_tracer()
    with tracer.start_span(buy_sub.__name__, child_of=get_current_span()) as span:
        with span_in_context(span):
            qiwi = payment_info.qiwi
            #TODO some pay logic

            delivery_info = producer.PostRole(
                command='post',
                user_id=payment_info.uuid,
                role=payment_info.sub_type
            )
            await producer.send_rabbitmq(delivery_info)

            return "success"
