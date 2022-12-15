import streamlit as st
import streamlit.components.v1 as components
import pandas as pd
from pyvis.network import Network
import plotly.express as px
import plotly.graph_objects as go
import networkx as nx

fourth_link = pd.read_csv('data/links_10402_grouped.csv')
fourth_node = pd.read_csv('data/nodes_10402.csv')
fifth_link = pd.read_csv('data/links_10504.csv')
fifth_node = pd.read_csv('data/nodes_10504.csv')
outsideClass = pd.read_csv('data/outside_class_data_10402.csv')

###Creating the fourth grade network graph

# Generate a networkx graph
G = nx.from_pandas_edgelist(fourth_link, 'Source', 'Target')

# Give the graph a name
G.name = 'CLAVES Social Network - Fourth Grade Yonkers'

# Obtain general information of graph
print(nx.info(G))

# Get graph density
density = nx.density(G)
print("Network density:", density)

##fourth grade

net = Network()

net.add_nodes = (['student 2',
         'student 3',
         'student 4',
         'student 5',
         'student 6',
         'student 7',
         'student 8',
         'student 9',
         'student 10',
         'student 12',
         'student 13',
         'student 14',
         'student 15',
         'student 16',
         'student 17',
         'student 18',
         'student 19',
         'student 20',
         'student 21',
         'student 22'], value = [1, 1, 1.666667, 0, 1.333333333, 1, 0, 0, 0, 1.45454545, 2.1111111, 0, 2, 0, 0, 0, 0, 2.16666667, 1.25])


net.add_edge('student 8', 'student 3')
net.add_edge('student 8', 'student 21')
net.add_edge('student 8', 'student 22')
net.add_edge('student 21', 'student 2')
net.add_edge('student 21', 'student 3')
net.add_edge('student 21', 'student 6')
net.add_edge('student 21', 'student 7')
net.add_edge('student 21', 'student 8')
net.add_edge('student 21', 'student 22')
net.add_edge('student 4', 'student 6')
net.add_edge('student 4', 'student 9')
net.add_edge('student 4', 'student 13')
net.add_edge('student 4', 'student 15')
net.add_edge('student 4', 'student 22')
net.add_edge('student 7', 'student 2')
net.add_edge('student 7', 'student 3')
net.add_edge('student 7', 'student 6')
net.add_edge('student 7', 'student 8')
net.add_edge('student 7', 'student 21'),
net.add_edge('student 7', 'student 22'),
net.add_edge('student 5', 'student 7'),
net.add_edge('student 5', 'student 16'),
net.add_edge('student 5', 'student 17'),
net.add_edge('student 5', 'student 18'),
net.add_edge('student 5', 'student 19'),
                  ('student 5', 'student 20'),
                  ('student 3', 'student 2'),
                  ('student 3', 'student 8'),
                  ('student 3', 'student 13'),
                  ('student 3', 'student 21'),
                  ('student 22', 'student 2'),
                  ('student 22', 'student 3'),
                  ('student 22', 'student 6'),
                  ('student 22', 'student 8'),
                  ('student 22', 'student 9'),
                  ('student 22', 'student 13'),
                  ('student 22', 'student 15'),
                  ('student 22', 'student 21'),
                  ('student 13', 'student 3'),
                  ('student 13', 'student 4'),
                  ('student 13', 'student 6'),
                  ('student 13', 'student 7'),
                  ('student 13', 'student 8'),
                  ('student 13', 'student 9'),
                  ('student 13', 'student 15'),
                  ('student 13', 'student 16'),
                  ('student 13', 'student 18'),
                  ('student 13', 'student 21'),
                  ('student 13', 'student 22'),
                  ('student 14', 'student 2'),
                  ('student 14', 'student 4'),
                  ('student 14', 'student 6'),
                  ('student 14', 'student 7'),
                  ('student 14', 'student 8'),
                  ('student 14', 'student 9'),
                  ('student 14', 'student 12'),
                  ('student 14', 'student 13'),
                  ('student 14', 'student 15'),
                  ('student 16', 'student 5'),
                  ('student 16', 'student 10'),
                  ('student 16', 'student 16'),
                  ('student 16', 'student 17'),
                  ('student 16', 'student 18'),
                  ('student 16', 'student 19'),
                  ('student 16', 'student 20')])

st.title("CLAVES Social Networks")
st.subheader("A closer look at student responses to the social network survey from 2021-2022 data")
class_list = ['Fourth Grade Yonkers', 'Fifth Grade Yonkers']
selected_class = st.multiselect('Select class to visualize', class_list)
if len(selected_class) == 0:
   st.text('Please choose at least 1 class to get started')
# Create network graph when user selects >= 1 item
else:
    # Create network graph when user selects >= 1 item

    # Create networkx graph object from pandas dataframe
    G = nx.from_pandas_edgelist(fourth_link, 'Source', 'Target')

    # Initiate PyVis network object
    soc_net = Network(height='465px', bgcolor='#222222', font_color='white')

    # Take Networkx graph and translate it to a PyVis graph format
    soc_net.from_nx(G)

    # Generate network with specific layout settings
    soc_net.repulsion(node_distance=420, central_gravity=0.33,
                       spring_length=110, spring_strength=0.10,
                       damping=0.95)

    try:
        path = '/tmp'
        soc_net.save_graph(f'{path}/pyvis_graph.html')
        HtmlFile = open(f'{path}/pyvis_graph.html', 'r', encoding='utf-8')

        # Save and read graph as HTML file (locally)
    except:
        path = '/html_files'
        soc_net.save_graph(f'{path}/pyvis_graph.html')
        HtmlFile = open(f'{path}/pyvis_graph.html', 'r', encoding='utf-8')

        # Load HTML file in HTML component for display on Streamlit page
    components.html(HtmlFile.read(), height=435)


st.write(fourth_link)
st.write(fourth_node)
st.write(fifth_link)
st.write(fifth_node)

##Fifth grade nodes and edges

G = nx.Graph()

G.add_nodes_from([
    ('student 12', {"Language Used": 1.2}),
    ('student 14', {"Language Used": 1}),
    ('student 18', {"Language Used": 1.294117647059}),
    ('student 2', {"Language Used": 1}),
    ('student 21', {"Language Used": 1.571428571429}),
    ('student 24', {"Language Used": 2}),
    ('student 25', {"Language Used": 2}),
    ('student 26', {"Language Used": 1.3636363636363}),
    ('student 27', {"Language Used": 1.5}),
    ('student 4', {"Language Used": 1}),
    ('student 8', {"Language Used": 2.45}),
    ('student 3', {"Language Used": 0}),
    ('student 6', {"Language Used": 0}),
    ('student 7', {"Language Used": 0}),
    ('student 9', {"Language Used": 0}),
    ('student 15', {"Language Used": 0}),
    ('student 16', {"Language Used": 0}),
    ('student 22', {"Language Used": 0}),
    ('student 13', {"Language Used": 0}),
    ('student 5', {"Language Used": 0}),
    ('student 10', {"Language Used": 0}),
    ('student 17', {"Language Used": 0}),
    ('student 19', {"Language Used": 0}),
    ('student 20', {"Language Used": 0})
])

list(fifth_link[['Source', 'Target']].itertuples(index=False, name=None))
###for row in fifth_link.itertuples(index=False):
    ##print(row)

G.add_edges_from([
    ('student 25', 'student 5'),
    ('student 25', 'student 7'),
    ('student 25', 'student 18'),
    ('student 25', 'student 20'),
    ('student 25', 'student 24'),
    ('student 25', 'student 21'),
    ('student 26', 'student 18'),
    ('student 26', 'student 2'),
    ('student 26', 'student 3'),
    ('student 26', 'student 4'),
    ('student 26', 'student 12'),
    ('student 26', 'student 14'),
    ('student 26', 'student 15'),
    ('student 26', 'student 16'),
    ('student 26', 'student 18'),
    ('student 26', 'student 21'),
    ('student 26', 'student 27'),
    ('student 4', 'student 1'),
    ('student 4', 'student 3'),
    ('student 4', 'student 5'),
    ('student 2', 'student 1'),
    ('student 2', 'student 3'),
    ('student 2','student 12'),
    ('student 2','student 16'),
    ('student 2','student 17'),
    ('student 2','student 23'),
    ('student 2','student 26'),
    ('student 2','student 27'),
    ('student 14','student 13'),
    ('student 14','student 15'),
    ('student 14','student 17'),
    ('student 14','student 26'),
    ('student 8','student 1'),
    ('student 8','student 2'),
    ('student 8','student 3'),
    ('student 8','student 4'),
    ('student 8','student 5'),
    ('student 8','student 6'),
    ('student 8','student 7'),
    ('student 8','student 8'),
    ('student 8','student 9'),
    ('student 8','student 10'),
    ('student 8', 'student 11'),
    ('student 8', 'student 14'),
    ('student 8','student 15'),
    ('student 8', 'student 16'),
    ('student 8', 'student 17'),
    ('student 8', 'student 18'),
    ('student 8', 'student 20'),
    ('student 8', 'student 21'),
    ('student 8', 'student 24'),
    ('student 8', 'student 26'),
    ('student 8', 'student 27'),
    ('student 27', 'student 1'),
    ('student 27', 'student 2'),
    ('student 27', 'student 3'),
    ('student 27','student 26'),
    ('student 24', 'student 5'),
    ('student 24', 'student 7'),
    ('student 24', 'student 8'),
    ('student 24','student 10'),
    ('student 24', 'student 11'),
    ('student 24','student 16'),
    ('student 24','student 18'),
    ('student 24','student 19'),
    ('student 24','student 20'),
    ('student 24', 'student 21'),
    ('student 24', 'student 22'),
    ('student 24', 'student 25'),
    ('student 21','student 1'),
    ('student 21', 'student 3'),
    ('student 21','student 4'),
    ('student 21', 'student 6'),
    ('student 21','student 16'),
    ('student 21','student 20'),
    ('student 21', 'student 27'),
    ('student 18', 'student 4'),
    ('student 18', 'student 5'),
    ('student 18', 'student 7'),
    ('student 18', 'student 8'),
    ('student 18', 'student 9'),
    ('student 18', 'student 11'),
    ('student 18', 'student 15'),
    ('student 18', 'student 16'),
    ('student 18', 'student 18'),
    ('student 18', 'student 19'),
    ('student 18', 'student 20'),
    ('student 18', 'student 21'),
    ('student 18', 'student 22'),
    ('student 18', 'student 24'),
    ('student 18', 'student 25'),
    ('student 18', 'student 27'),
    ('student 18', 'student 12'),
    ('student 12', 'student 1'),
    ('student 12', 'student 2'),
    ('student 12', 'student 3'),
    ('student 12', 'student 15'),
    ('student 12', 'student 26')
])

edge_x = []
edge_y = []
for edge in G.edges():
    x0, y0 = G.nodes[edge[0]]['pos']
    x1, y1 = G.nodes[edge[1]]["pos"]
    edge_x.append(x0)
    edge_x.append(x1)
    edge_x.append(None)
    edge_y.append(y0)
    edge_y.append(y1)
    edge_y.append(None)

edge_trace = go.Scatter(
    x=edge_x, y=edge_y,
    line=dict(width=0.5, color='#888'),
    hoverinfo='none',
    mode='lines')

node_x = []
node_y = []
for node in G.nodes():
    x, y = G.nodes[node]['pos']
    node_x.append(x)
    node_y.append(y)

node_trace = go.Scatter(
    x=node_x, y=node_y,
    mode='markers',
    hoverinfo='text',
    marker=dict(
        showscale=True,
        # colorscale options
        #'Greys' | 'YlGnBu' | 'Greens' | 'YlOrRd' | 'Bluered' | 'RdBu' |
        #'Reds' | 'Blues' | 'Picnic' | 'Rainbow' | 'Portland' | 'Jet' |
        #'Hot' | 'Blackbody' | 'Earth' | 'Electric' | 'Viridis' |
        colorscale='YlGnBu',
        reversescale=True,
        color=[],
        size=10,
        colorbar=dict(
            thickness=15,
            title='Node Connections',
            xanchor='left',
            titleside='right'
        ),
        line_width=2))


fig = go.Figure(data=[edge_trace, node_trace],
             layout=go.Layout(
                title='<br>Network graph made with Python',
                titlefont_size=16,
                showlegend=False,
                hovermode='closest',
                margin=dict(b=20,l=5,r=5,t=40),
                annotations=[ dict(
                    text="Python code: <a href='https://plotly.com/ipython-notebooks/network-graphs/'> https://plotly.com/ipython-notebooks/network-graphs/</a>",
                    showarrow=False,
                    xref="paper", yref="paper",
                    x=0.005, y=-0.002 ) ],
                xaxis=dict(showgrid=False, zeroline=False, showticklabels=False),
                yaxis=dict(showgrid=False, zeroline=False, showticklabels=False))
                )
st.plotly_chart(fig)

##Fourth Grade Nodes and Edges###

G.add_nodes_from([
    ('student 2', {"Language Used": 0}),
    ('student 3', {"Language Used": 1}),
    ('student 4', {"Language Used": 1}),
    ('student 5', {"Language Used": 1.666667}),
    ('student 6', {"Language Used": 0}),
    ('student 7', {"Language Used": 1.333333333}),
    ('student 8', {"Language Used": 1}),
    ('student 9', {"Language Used": 0}),
    ('student 10', {"Language Used": 0}),
    ('student 12', {"Language Used": 0}),
    ('student 13', {"Language Used": 1.45454545}),
    ('student 14', {"Language Used": 2.1111111}),
    ('student 15', {"Language Used": 0}),
    ('student 16', {"Language Used": 2}),
    ('student 17', {"Language Used": 0}),
    ('student 18', {"Language Used": 0}),
    ('student 19', {"Language Used": 0}),
    ('student 20', {"Language Used": 0}),
    ('student 21', {"Language Used": 2.16666667}),
    ('student 22', {"Language Used": 1.25})
])

list(fourth_link[['Source', 'Target']].itertuples(index=False, name=None))
for row in fourth_link.itertuples(index=False):
    print(row)

G.add_edges_from([('student 8', 'student 3'),
                  ('student 8', 'student 21'),
                  ('student 8', 'student 22'),
                  ('student 21', 'student 2'),
                  ('student 21', 'student 3'),
                  ('student 21', 'student 6'),
                  ('student 21', 'student 7'),
                  ('student 21', 'student 8'),
                  ('student 21', 'student 22'),
                  ('student 4', 'student 6'),
                  ('student 4', 'student 9'),
                  ('student 4', 'student 13'),
                  ('student 4', 'student 15'),
                  ('student 4', 'student 22'),
                  ('student 7', 'student 2'),
                  ('student 7', 'student 3'),
                  ('student 7', 'student 6'),
                  ('student 7', 'student 8'),
                  ('student 7', 'student 21'),
                  ('student 7', 'student 22'),
                  ('student 5', 'student 7'),
                  ('student 5', 'student 16'),
                  ('student 5', 'student 17'),
                  ('student 5', 'student 18'),
                  ('student 5', 'student 19'),
                  ('student 5', 'student 20'),
                  ('student 3', 'student 2'),
                  ('student 3', 'student 8'),
                  ('student 3', 'student 13'),
                  ('student 3', 'student 21'),
                  ('student 22', 'student 2'),
                  ('student 22', 'student 3'),
                  ('student 22', 'student 6'),
                  ('student 22', 'student 8'),
                  ('student 22', 'student 9'),
                  ('student 22', 'student 13'),
                  ('student 22', 'student 15'),
                  ('student 22', 'student 21'),
                  ('student 13', 'student 3'),
                  ('student 13', 'student 4'),
                  ('student 13', 'student 6'),
                  ('student 13', 'student 7'),
                  ('student 13', 'student 8'),
                  ('student 13', 'student 9'),
                  ('student 13', 'student 15'),
                  ('student 13', 'student 16'),
                  ('student 13', 'student 18'),
                  ('student 13', 'student 21'),
                  ('student 13', 'student 22'),
                  ('student 14', 'student 2'),
                  ('student 14', 'student 4'),
                  ('student 14', 'student 6'),
                  ('student 14', 'student 7'),
                  ('student 14', 'student 8'),
                  ('student 14', 'student 9'),
                  ('student 14', 'student 12'),
                  ('student 14', 'student 13'),
                  ('student 14', 'student 15'),
                  ('student 16', 'student 5'),
                  ('student 16', 'student 10'),
                  ('student 16', 'student 16'),
                  ('student 16', 'student 17'),
                  ('student 16', 'student 18'),
                  ('student 16', 'student 19'),
                  ('student 16', 'student 20')])

if len(selected_class) == 0:
   st.text('Please choose at least 1 class to get started')
# Create network graph when user selects >= 1 item
else:
    # Create network graph when user selects >= 1 item

    # Create networkx graph object from pandas dataframe
    G = nx.from_pandas_edgelist(fourth_link, 'Source', 'Target')

    # Initiate PyVis network object
    soc_net = Network(height='465px', bgcolor='#222222', font_color='white')

    # Take Networkx graph and translate it to a PyVis graph format
    soc_net.from_nx(G)

    # Generate network with specific layout settings
    soc_net.repulsion(node_distance=420, central_gravity=0.33,
                       spring_length=110, spring_strength=0.10,
                       damping=0.95)




