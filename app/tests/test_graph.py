from app.graph.workflow import workflow
from app.schemas.chat import WorkflowState


def test_graph_runs():
    state: WorkflowState = {
        "user_query": "Just a test",
        "intent": None,
        "product_id": None,
        "prod_sale_use_num": None,
        "date": None,
        "quantity": None,
        "reservation_id": None,
        "order_id": None,
        "messages": [],
    }
    workflow.invoke(state)
    assert True
