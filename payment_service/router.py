from fastapi import APIRouter, status, HTTPException, Depends
from schemas import Sub, BuySub
import services
import logging
import opentracing
from jaeger_client import Tracer
from opentracing_instrumentation.request_context import get_current_span, span_in_context

router = APIRouter(
    tags=['Payment'],
    prefix='/payment'
)


@router.post(
    '/buy',
    status_code=200,
    response_model=dict
)
async def buy_sub(pay_info: BuySub):
    tracer = opentracing.global_tracer()
    with tracer.start_span(buy_sub.__name__, child_of=get_current_span()) as span:
        with span_in_context(span):
            pay_stat = await services.buy_sub(pay_info)
            return {'result': pay_stat}




