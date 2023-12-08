import pandas as pd
import plotly.express as px

# Read the data from the text file
data = []
with open('top_10_service_cost_past_six_months.txt', 'r') as file:
    lines = file.readlines()
    columns = lines[0].strip().split('\t')
    for line in lines[1:]:
        values = line.strip().split('\t')
        service = values[0]
        costs = [float(cost) for cost in values[1:]]
        data.append([service] + costs)  # Include costs for all months

# Create a DataFrame
df = pd.DataFrame(data, columns=columns)

# Set 'Service' column as the index
df.set_index('Service', inplace=True)

# Transpose the DataFrame to have months as columns
df_transposed = df.transpose()

# Reverse the order of columns to have latest and first month from left to right
df_transposed = df_transposed.iloc[:, ::-1]

# Create the bar chart using Plotly
fig = px.bar(df_transposed, x=df_transposed.index, y=df_transposed.columns,
             title='Top AWS Service Costs by Month',
             labels={'index': 'Month', 'value': 'Cost ($)'},
             height=800)  # Increase the height for taller columns

# Customize the text that appears on the bars and increase text size
fig.update_traces(texttemplate='%{y:$2:.2f}', textposition='outside',
                  hoverinfo='text', hovertext='%{y:$,.2f}',
                  marker=dict(line=dict(width=0)))  # Set the line width to 0

# Update layout
fig.update_layout(
    xaxis_title=None,
    yaxis_title='Cost ($)',
    xaxis_tickangle=-45,
    autosize=True,
    margin=dict(t=200),
    showlegend=True,
    font=dict(size=14)  # Increase the font size of the axis labels and title
)

# Save the plot as a PNG image
fig.write_image('aws_service_cost_top_chart_plotly.png', width=1600, height=1200)

# Flip the x-axis
fig.update_xaxes(autorange="reversed")

# Show the plot
fig.show()
