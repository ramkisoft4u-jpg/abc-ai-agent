from langgraph.graph import StateGraph, END
from app.schemas.chat import WorkflowState
from app.agents.orchestrator_agent import orchestrator_node
from app.agents.demand_planning_agent import demand_planning_node
from app.agents.order_agent import order_node
from app.agents.reservation_agent import reservation_node


graph = StateGraph(WorkflowState)

graph.add_node("orchestrator", orchestrator_node)
graph.add_node("demand_planning", demand_planning_node)
graph.add_node("order", order_node)
graph.add_node("reservation", reservation_node)

graph.set_entry_point("orchestrator")


def route(state: WorkflowState):
    intent = state.get("intent")
    if intent == "create_order_with_reservation":
        return "demand_planning"
    if intent == "delete_reservation":
        return "reservation"
    return END


graph.add_conditional_edges(
    "orchestrator",
    route,
    {
        "demand_planning": "demand_planning",
        "reservation": "reservation",
        END: END,
    },
)

graph.add_edge("demand_planning", "order")
graph.add_edge("order", END)
graph.add_edge("reservation", END)

workflow = graph.compile()
