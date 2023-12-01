import plotly.graph_objects as go

# Example data
labels = ['Product A', 'Product B', 'Product C', 'Product D']
values = [450, 250, 300, 500]

# Choose a color palette for the pie chart
colors = ['#7f8c8d', '#3498db', '#2ecc71', '#e74c3c']

# Create the pie chart
fig = go.Figure(data=[go.Pie(labels=labels, values=values)])

# Customize the layout and appearance
fig.update_traces(
    hoverinfo='label+percent', textinfo='value', textfont_size=14,
    marker=dict(colors=colors, line=dict(color='#000000', width=2))
)

# Update the layout for a professional look
fig.update_layout(
    title_text='Sales Distribution by Product',
    title_font=dict(size=18, color='white', family='Arial, sans-serif'),
    showlegend=True,
    legend_font=dict(size=14, color='white'),
    paper_bgcolor='rgba(35, 37, 38, 1)',
    plot_bgcolor='rgba(35, 37, 38, 1)',
    legend=dict(
        orientation="h",
        yanchor="bottom",
        y=-0.2,
        xanchor="center",
        x=0.5
    )
)

# Customize hover template
fig.update_traces(
    hovertemplate='<b>%{label}</b><br>%{percent}<br><extra></extra>'
)

fig.show()
