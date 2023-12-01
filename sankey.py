import plotly.graph_objects as go

journeys = [
    "A,B,C",
    "B,A",
    "C,A",
    "A,C",
]


start_node = "Start"
nodes = {start_node}


for journey in journeys:
    nodes.update(journey.split(','))

node_order = [start_node, "A", "B", "C"]
node_to_index = {node: i for i, node in enumerate(node_order)}


source = []
target = []
value = []

for journey in journeys:
    path = journey.split(',')

    path.insert(0, start_node)
    for i in range(len(path)-1):
        src = node_to_index[path[i]]
        tgt = node_to_index[path[i+1]]
        source.append(src)
        target.append(tgt)
        value.append(1)


labels = [None] * len(node_to_index)
for node, index in node_to_index.items():
    labels[index] = node


# Improved color scheme for nodes and links
node_colors = ['#7f8c8d', '#3498db', '#2ecc71', '#e74c3c', '#f1c40f']
link_colors = {
    'forward': 'rgba(46, 204, 113, 0.6)',  # Softer green for forward
    'backward': 'rgba(231, 76, 60, 0.6)'    # Softer red for backward
}

colors = [
    link_colors['forward'] if source[i] < target[i] else link_colors['backward']
    for i in range(len(source))
]


# # Initialize the colors list
# colors = []

# for i in range(len(source)):
#     # Start node to any other node is considered a forward journey
#     if source[i] == node_to_index[start_node]:
#         colors.append('rgba(50, 168, 82, 0.8)')  # Green for forward
#     # Journey from a node with a lower index to a higher index is considered forward
#     elif source[i] < target[i]:
#         colors.append('rgba(50, 168, 82, 0.8)')  # Green for forward
#     else:
#         colors.append('rgba(255, 0, 0, 0.8)')  # Red for backward

max_value = max(value)
normalized_value = [v / max_value * 10 for v in value]


# Create the figure
fig = go.Figure(data=[go.Sankey(
    node=dict(
        pad=20,
        thickness=30,
        line=dict(color="black", width=0.5),
        label=labels,
        color=node_colors,
        hoverinfo='all',
        hovertemplate='%{label}<extra></extra>',  # Custom hovertemplate for nodes
    ),
    link=dict(
        source=source,
        target=target,
        value=normalized_value,
        color=colors,
        hoverinfo='all',
        hovertemplate='%{source.label} to %{target.label}: %{value}<extra></extra>',  # Custom hovertemplate for links
    )
)])



# Update the layout for a more professional look
fig.update_layout(
    title_text="Conversational Journey Flows",
    font=dict(
        size=14,
        color='white',
        family='Arial, sans-serif'
    ),
    paper_bgcolor='rgba(35, 37, 38, 1)',
    plot_bgcolor='rgba(35, 37, 38, 1)',
    hovermode='x'
)

# # Add annotations and hover text for better clarity and information
# for i, (src, tgt) in enumerate(zip(source, target)):
#     fig['data'][0]['link']['hoverinfo'] = 'none'  # Turn off link hover info
#     # Custom hover text for nodes
#     fig['data'][0]['node']['hoverinfo'] = 'all'
#     fig['data'][0]['node']['hovertext'] = [
#         f"{label}: Total conversations started here" if label == start_node else f"{label}: Conversations passing through"
#         for label in labels
#     ]

fig.show()
