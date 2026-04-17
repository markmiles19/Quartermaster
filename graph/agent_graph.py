from langgraph.graph import StateGraph
from nodes.observe import observe
from nodes.analyze import analyze
from nodes.plan import plan
from nodes.act import act

def build_graph():
    graph = StateGraph(dict)

    graph.add_node("observe", observe)
    graph.add_node("analyze", analyze)
    graph.add_node("plan", plan)
    graph.add_node("act", act)

    graph.set_entry_point("observe")

    graph.add_edge("observe", "analyze")
    graph.add_edge("analyze", "plan")
    graph.add_edge("plan", "act")

    return graph.compile()

graph = build_graph()