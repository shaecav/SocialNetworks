import streamlit as st
import streamlit.components.v1 as components
import pandas as pd
import requests
from pyvis.network import Network
import plotly.express as px
import plotly.graph_objects as go
import networkx as nx
import matplotlib.pyplot as plt
from streamlit_agraph import agraph, Node, Edge, Config
from streamlit_lottie import st_lottie
from PIL import Image
from streamlit_plotly_events import plotly_events



fourth_link = pd.read_csv('data/links_10402_grouped.csv')
fourth_node = pd.read_csv('data/nodes_10402.csv')
fifth_link = pd.read_csv('data/links_10504.csv')
fifth_node = pd.read_csv('data/nodes_10504.csv')
outsideClass = pd.read_csv('data/outside_class_data_10402.csv')
fourth_classification = pd.read_csv('data/10402 Classification.csv')
fifth_classification = pd.read_csv('data/10504 Classification.csv')

def load_lottieurl(url: str):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

lottie_url = "https://assets2.lottiefiles.com/packages/lf20_ovqgenlq.json"
lottie_animation = load_lottieurl(lottie_url)
st_lottie(lottie_animation, key="animation", height=200)

col1, col2 = st.columns(2)

with col1:
    st.title("CLAVES Social Networks")



#opening the image

CLAVESimage = Image.open('CLAVES logo png.png')



#displaying the image on streamlit app


with col2:
   st.image(CLAVESimage, caption='')

st.write("_A closer look at student responses to the social network survey from 2021-2022 data_")

class_list = ['10402', '10504']

st.sidebar.title('Select Class to Begin')
page = st.sidebar.radio('', ('10402', '10504'))

if page == "10504":
    st.subheader("10504 Social Network Data: who students like to hang out with in their class")
    key_image = Image.open('Screen Shot 2022-12-15 at 6.11.48 PM.png')
    with st.expander("See key"):
        st.write("""
        The social network graph below reflects the student social network survey data from class 10504. 
        Click on a node to engage with it.""")
        st.image(key_image)

    nodes = []
    edges = []
    nodes.append(Node(id="student 12",
                   label="student 12",
                   size=12,
                  color="#B73C27",
                  shape="circularImage",
                  image="CLAVES logo png.png")
            )
    nodes.append(Node(id="student 14",
                   label='student 14',
                   size=10, color="#B73C27",
                   shape="circularImage",
                   image="CLAVES logo png.png")
            )
    nodes.append(Node(id="student 18",
                   label='student 18',color="#B73C27",
                   size=13, shape = "circularImage", image = "CLAVES logo png.png"))
    nodes.append(Node(id="student 2",
                   label='student 2', color='#28327B',
                   size=10))
    nodes.append(Node(id="student 21",
                   label='student 21',
                   size=18, color="#B73C27", shape = "circularImage", image = "CLAVES logo png.png"))
    nodes.append(Node(id="student 24",
                   label="student 24",color='#28327B',
                   size=20)
            )
    nodes.append(Node(id="student 25",
                   label="student 25",
                   size=20,
                  color="#B73C27",
                  shape="circularImage",
                  image="CLAVES logo png.png")
            )
    nodes.append(Node(id="student 26",
                   label="student 26",
                   size=14,
                  color="#B73C27",
                  shape="circularImage",
                  image="CLAVES logo png.png")
            )
    nodes.append(Node(id="student 27",
                   label="student 27",
                   size=15,
                  color="#B73C27",
                  shape="circularImage",
                  image="CLAVES logo png.png")
            )
    nodes.append(Node(id="student 4",
                   label="student 4",
                   size=10,
                  color="#B73C27",
                  shape="circularImage",
                  image="CLAVES logo png.png")
            )
    nodes.append(Node(id="student 8",
                   label="student 8", color='#28327B',
                   size=25)
            )
    nodes.append(Node(id="student 3",
                   label="student 3",
                   size=5, color= "black")
            )
    nodes.append(Node(id="student 6",
                   label="student 6",
                   size=5, color= "black"))
    nodes.append(Node(id="student 7",
                   label="student 7",
                   size=5, color= "black"))
    nodes.append(Node(id="student 9",
                   label="student 9",
                   size=5, color= "black"))
    nodes.append(Node(id="student 15",
                   label="student 15",
                   size=5, color= "black"))
    nodes.append(Node(id="student 16",
                   label="student 16",
                   size=5, color= "black"))
    nodes.append(Node(id="student 22",
                   label="student 22",
                   size=5, color= "black"))
    nodes.append(Node(id="student 13",
                   label="student 13",
                   size=5, color= "black"))
    nodes.append(Node(id="student 5",
                   label="student 5",
                   size=5, color= "black"))
    nodes.append(Node(id="student 10",
                   label="student 10",
                   size=5, color= "black"))
    nodes.append(Node(id="student 17",
                   label="student 17",
                   size=5, color= "black"))
    nodes.append(Node(id="student 19",
                   label="student 19",
                   size=5, color= "black"))
    nodes.append(Node(id="student 20",
                   label="student 20",
                   size=5, color= "black"))

    ##Adding in the edges##

    edges.append( Edge(source="student 25",
                   #label="H",
                   target="student 5"
                   )
            )
    edges.append( Edge(source="student 25",
                  # label="H",
                   target="student 7"
                   )
            )
    edges.append( Edge(source="student 25",
                  # label="H",
                   target="student 18"
                   )
            )
    edges.append( Edge(source="student 25",
                   #label="H",
                   target="student 20"
                   )
            )
    edges.append( Edge(source="student 25",
                   #label="H",
                   target="student 21"
                   )
            )
    edges.append( Edge(source="student 25",
                  # label="H",
                   target="student 24"
                   )
            )
    edges.append( Edge(source="student 25",
                   #label="H",
                   target="student 21"
                   )
            )
    edges.append( Edge(source="student 26",
                  # label="H",
                   target="student 2"
                   )
            )
    edges.append( Edge(source="student 26",
                   #label="H",
                   target="student 3"
                   )
            )
    edges.append( Edge(source="student 26",
                  # label="H",
                   target="student 4"
                   )
            )
    edges.append( Edge(source="student 26",
                   #label="H",
                   target="student 12"
                   )
            )
    edges.append( Edge(source="student 26",
                  # label="H",
                   target="student 14"
                   )
            )
    edges.append( Edge(source="student 26",
                  # label="H",
                   target="student 15"
                   )
            )
    edges.append( Edge(source="student 26",
                   #label="H",
                   target="student 16"
                   )
            )
    edges.append( Edge(source="student 26",
                  # label="H",
                   target="student 18"
                   )
            )
    edges.append( Edge(source="student 26",
                  # label="H",
                   target="student 21"
                   )
            )

    edges.append( Edge(source="student 26",
                  # label="H",
                   target="student 27"
                   )
            )
    edges.append( Edge(source="student 2",
                   #label="H",
                   target="student 1"
                   )
            )
    edges.append( Edge(source="student 4",
                  # label="H",
                   target="student 3"
                   )
            )
    edges.append( Edge(source="student 4",
                  # label="H",
                   target="student 5"
                   )
            )

    edges.append( Edge(source="student 2",
                  # label="H",
                   target="student 1"
                   )
            )

    edges.append( Edge(source="student 2",
                  # label="H",
                   target="student 3"
                   )
            )
    edges.append( Edge(source="student 2",
                   #label="H",
                   target="student 12"
                   )
            )

    edges.append( Edge(source="student 2",
                  # label="H",
                   target="student 16"
                   )
            )
    edges.append( Edge(source="student 2",
                  # label="H",
                   target="student 17"
                   )
            )
    edges.append( Edge(source="student 2",
                  # label="H",
                   target="student 23"
                   )
            )
    edges.append( Edge(source="student 2",
                  # label="H",
                   target="student 26"
                   )
            )
    edges.append( Edge(source="student 2",
                  #label="H",
                   target="student 27"
                   )
            )
    edges.append( Edge(source="student 14",
                   #label="H",
                   target="student 13"
                   )
            )
    edges.append( Edge(source="student 14",
                  # label="H",
                   target="student 15"
                   )
            )
    edges.append( Edge(source="student 14",
                  # label="H",
                   target="student 17"
                   )
            )
    edges.append( Edge(source="student 14",
                  # label="H",
                   target="student 26"
                   )
            )
    edges.append( Edge(source="student 8",
                  # label="H",
                   target="student 1"
                   )
            )
    edges.append( Edge(source="student 8",
                  # label="H",
                   target="student 2"
                   )
            )
    edges.append( Edge(source="student 8",
                   #label="H",
                   target="student 3"
                   )
            )
    edges.append( Edge(source="student 8",
                  # label="H",
                   target="student 4"
                   )
            )
    edges.append( Edge(source="student 8",
                  # label="H",
                   target="student 5"
                   )
            )
    edges.append( Edge(source="student 8",
                   #label="H",
                   target="student 6"
                   )
            )

    edges.append( Edge(source="student 8",
                  # label="H",
                   target="student 7"
                   )
            )
    edges.append( Edge(source="student 8",
                  # label="H",
                   target="student 9"
                   )
            )
    edges.append( Edge(source="student 8",
                  # label="H",
                   target="student 10"
                   )
            )
    edges.append( Edge(source="student 8",
                  # label="H",
                   target="student 11"
                   )
            )
    edges.append( Edge(source="student 8",
                  # label="H",
                   target="student 14"
                   )
            )
    edges.append( Edge(source="student 8",
                  # label="H",
                   target="student 15"
                   )
            )
    edges.append( Edge(source="student 8",
                  # label="H",
                   target="student 16"
                   )
            )
    edges.append( Edge(source="student 8",
                   #label="H",
                   target="student 17"
                   )
            )
    edges.append( Edge(source="student 8",
                  # label="H",
                   target="student 18"
                   )
            )
    edges.append( Edge(source="student 8",
                  # label="H",
                   target="student 20"
                   )
            )
    edges.append( Edge(source="student 8",
                  # label="H",
                   target="student 21"
                   )
            )
    edges.append( Edge(source="student 8",
                  # label="H",
                   target="student 24"
                   )
            )
    edges.append( Edge(source="student 8",
                   #label="H",
                   target="student 26"
                   )
            )
    edges.append( Edge(source="student 8",
                   #label="H",
                   target="student 27"
                   )
            )
    edges.append( Edge(source="student 27",
                   #label="H",
                   target="student 1"
                   )
            )
    edges.append( Edge(source="student 27",
                   #label="H",
                   target="student 2"
                   )
            )
    edges.append( Edge(source="student 27",
                   #label="H",
                   target="student 3"
                   )
            )
    edges.append( Edge(source="student 27",
                  # label="H",
                   target="student 26"
                   )
            )

    edges.append( Edge(source="student 24",
                  # label="H",
                   target="student 5"
                   )
            )
    edges.append( Edge(source="student 24",
                  # label="H",
                   target="student 7"
                   )
            )
    edges.append( Edge(source="student 24",
                   #label="H",
                   target="student 8"
                   )
            )
    edges.append( Edge(source="student 24",
                   #label="H",
                   target="student 10"
                   )
            )
    edges.append( Edge(source="student 24",
                   #label="H",
                   target="student 11"
                   )
            )
    edges.append( Edge(source="student 24",
                   #label="H",
                   target="student 16"
                   )
            )
    edges.append( Edge(source="student 24",
                   #label="H",
                   target="student 18"
                   )
            )
    edges.append( Edge(source="student 24",
                  # label="H",
                   target="student 19"
                   )
            )
    edges.append( Edge(source="student 24",
                   #label="H",
                   target="student 20"
                   )
            )
    edges.append( Edge(source="student 24",
                   #label="H",
                   target="student 21"
                   )
            )
    edges.append( Edge(source="student 24",
                   #label="H",
                   target="student 22"
                   )
            )
    edges.append( Edge(source="student 24",
                   #label="H",
                   target="student 25"
                   )
            )

    edges.append( Edge(source="student 21",
                   #label="H",
                   target="student 1"
                   )
            )
    edges.append( Edge(source="student 21",
                   #label="H",
                   target="student 3"
                   )
            )
    edges.append( Edge(source="student 21",
                   #label="H",
                   target="student 4"
                   )
            )
    edges.append( Edge(source="student 21",
                  # label="H",
                   target="student 6"
                   )
            )
    edges.append( Edge(source="student 21",
                  # label="H",
                   target="student 20"
                   )
            )
    edges.append( Edge(source="student 20",
                  # label="H",
                   target="student 16"
                   )
            )
    edges.append( Edge(source="student 21",
                  # label="H",
                   target="student 27"
                   )
            )

    edges.append( Edge(source="student 12",
                   #label="H",
                   target="student 26"
                   )
            )
    edges.append( Edge(source="student 12",
                  # label="H",
                   target="student 15"
                   )
            )
    edges.append( Edge(source="student 12",
                   #label="H",
                   target="student 3"
                   )
            )
    edges.append( Edge(source="student 12",
                   #label="H",
                   target="student 2"
                   )
            )
    edges.append( Edge(source="student 12",
                  # label="H",
                   target="student 1"
                   )
            )
    edges.append( Edge(source="student 18",
                  #label="H",
                   target="student 12"
                   )
            )
    edges.append( Edge(source="student 18",
                  # label="H",
                   target="student 27"
                   )
            )
    edges.append( Edge(source="student 18",
                   #label="H",
                   target="student 25"
                   )
            )
    edges.append( Edge(source="student 18",
                  # label="Hh",
                   target="student 24"
                   )
            )
    edges.append( Edge(source="student 18",
                   #label="H",
                   target="student 22"
                   )
            )
    edges.append( Edge(source="student 18",
                   #label="H",
                   target="student 21"
                   )
            )
    edges.append( Edge(source="student 18",
                   #label="H",
                   target="student 20"
                   )
            )
    edges.append( Edge(source="student 18",
                   #label="H",
                   target="student 19"
                   )
            )
    edges.append( Edge(source="student 18",
                  # label="H",
                   target="student 18"
                   )
            )
    edges.append( Edge(source="student 18",
                  # label="H",
                   target="student 16"
                   )
            )
    edges.append( Edge(source="student 18",
                  # label="H",
                   target="student 15"
                   )
            )
    edges.append( Edge(source="student 18",
                   #label="H",
                   target="student 11"
                   )
            )
    edges.append( Edge(source="student 18",
                  # label="H",
                   target="student 9"
                   )
            )
    edges.append( Edge(source="student 18",
                  # label="H",
                   target="student 8"
                   )
            )
    edges.append( Edge(source="student 18",
                  # label="H",
                   target="student 7"
                   )
            )
    edges.append( Edge(source="student 18",
                   #label="H",
                   target="student 5"
                   )
            )
    edges.append( Edge(source="student 18",
                  # label="H",
                   target="student 4"
                   )
            )

    config = Config(width=1300,
                height=700,
                nodeHighlightBehavior=True,
                highlightOpacity= .5
                )

    FifthGraph = agraph(nodes=nodes,
                      edges=edges,
                      config=config)

    fifth_select = st.selectbox('Learn more about the study participants:',
                                 options=fifth_classification['Student'].unique(), index=1)

    if fifth_select == 'student 14':
        st.subheader('Multilingual: No')
        st.subheader('Assigned Group: Heterogeneous')

    if fifth_select == 'student 18':
        st.subheader('Multilingual: No')
        st.subheader('Assigned Group: Heterogeneous')

    if fifth_select == 'student 4':
        st.subheader('Multilingual: Yes')
        st.subheader('Assigned Group: Heterogeneous')

    if fifth_select == 'student 21':
        st.subheader('Multilingual: Yes')
        st.subheader('Assigned Group: Homogeneous')

    if fifth_select == 'student 25':
        st.subheader('Multilingual: Yes')
        st.subheader('Assigned Group: Heterogeneous')

    if fifth_select == 'student 12':
        st.subheader('Multilingual: Yes')
        st.subheader('Assigned Group: Homogeneous')

    if fifth_select == 'student 26':
        st.subheader('Multilingual: Yes')
        st.subheader('Assigned Group: Homogeneous')

    if fifth_select == 'student 27':
        st.subheader('Multilingual: Yes')
        st.subheader('Assigned Group: Homogeneous')


##NOW FOR FOURTH GRADE###

if page == "10402":
    st.subheader("10402 Social Network Data: who students like to hang out with in their class")
    key_image = Image.open('Screen Shot 2022-12-15 at 6.11.48 PM.png')
    with st.expander("See key"):
        st.write("""
        The social network graph below reflects the student social network survey data from class 10402. 
        Find out more information about the selected students below.""")
        st.image(key_image)

    nodes = []
    edges = []

    ##node-ing along##

    nodes.append(Node(id="student 22",
                   label="student 22",
                   size=13, color='#28327B')
            )
    nodes.append(Node(id="student 21",
                   label="student 21",
                   size=22, color='#28327B')
            )
    nodes.append(Node(id="student 20",
                   label="student 20",
                   size=5, color='black')
            )
    nodes.append(Node(id="student 19",
                   label="student 19",
                   size=5, color='black')
            )
    nodes.append(Node(id="student 18",
                   label="student 18",
                   size=5, color='black')
            )
    nodes.append(Node(id="student 17",
                   label="student 17",
                   size=5, color='black')
            )
    nodes.append(Node(id="student 16",
                   label="student 16",
                   size=20, color="#B73C27")
            )
    nodes.append(Node(id="student 15",
                      label="student 15",
                      size=5, color="black")
                 )
    nodes.append(Node(id="student 14",
                      label="student 14",
                      size=21, color="#B73C27")
                 )
    nodes.append(Node(id="student 13",
                      label="student 13",
                      size=15, color="#B73C27")
                 )
    nodes.append(Node(id="student 12",
                      label="student 12",
                      size=5, color="black")
                 )
    nodes.append(Node(id="student 10",
                      label="student 10",
                      size=5, color="black")
                 )
    nodes.append(Node(id="student 9",
                      label="student 9",
                      size=5, color="black")
                 )
    nodes.append(Node(id="student 8",
                      label="student 8",
                      size=10, color="#B73C27")
                 )
    nodes.append(Node(id="student 7",
                      label="student 7",
                      size=13, color="#28327B")
                 )
    nodes.append(Node(id="student 6",
                      label="student 6",
                      size=5, color="black")
                 )
    nodes.append(Node(id="student 5",
                      label="student 5",
                      size=17, color="#B73C27")
                 )
    nodes.append(Node(id="student 4",
                      label="student 4",
                      size=10, color="#B73C27")
                 )
    nodes.append(Node(id="student 3",
                      label="student 3",
                      size=10, color="#B73C27")
                 )
    nodes.append(Node(id="student 2",
                      label="student 2",
                      size=5, color="black")
                 )
    nodes.append(Node(id="student 1",
                      label="student 1",
                      size=5,color='#B73C27'
                      )
                 )

    ###edging###
    edges.append(Edge(source="student 8",
                      target="student 3"
                      )
                 )
    edges.append(Edge(source="student 8",
                      target="student 21"
                      )
                 )
    edges.append(Edge(source="student 8",
                      target="student 22"
                      )
                 )
    edges.append(Edge(source="student 21",
                      target="student 2"
                      )
                 )
    edges.append(Edge(source="student 21",
                      target="student 3"
                      )
                 )
    edges.append(Edge(source="student 21",
                      target="student 6"
                      )
                 )
    edges.append(Edge(source="student 21",
                      target="student 7"
                      )
                 )
    edges.append(Edge(source="student 21",
                      target="student 8"
                      )
                 )
    edges.append(Edge(source="student 21",
                      target="student 22"
                      )
                 )
    edges.append(Edge(source="student 4",
                      target="student 6"
                      )
                 )
    edges.append(Edge(source="student 4",
                      target="student 9"
                      )
                 )
    edges.append(Edge(source="student 4",
                      target="student 15"
                      )
                 )
    edges.append(Edge(source="student 4",
                      target="student 22"
                      )
                 )
    edges.append(Edge(source="student 7",
                      target="student 2"
                      )
                 )

    edges.append(Edge(source="student 7",
                      target="student 3"
                      )
                 )
    edges.append(Edge(source="student 7",
                      target="student 6"
                      )
                 )
    edges.append(Edge(source="student 7",
                      target="student 8"
                      )
                 )
    edges.append(Edge(source="student 7",
                      target="student 21"
                      )
                 )
    edges.append(Edge(source="student 7",
                      target="student 22"
                      )
                 )
    edges.append(Edge(source="student 7",
                      target="student 3"
                      )
                 )
    edges.append(Edge(source="student 5",
                      target="student 7"
                      )
                 )
    edges.append(Edge(source="student 5",
                      target="student 16"
                      )
                 )
    edges.append(Edge(source="student 5",
                      target="student 17"
                      )
                 )
    edges.append(Edge(source="student 5",
                      target="student 18"
                      )
                 )
    edges.append(Edge(source="student 7",
                      target="student 19"
                      )
                 )
    edges.append(Edge(source="student 7",
                      target="student 20"
                      )
                 )
    edges.append(Edge(source="student 3",
                      target="student 2"
                      )
                 )
    edges.append(Edge(source="student 3",
                      target="student 8"
                      )
                 )
    edges.append(Edge(source="student 3",
                      target="student 13"
                      )
                 )
    edges.append(Edge(source="student 3",
                      target="student 21"
                      )
                 )
    edges.append(Edge(source="student 22",
                      target="student 2"
                      )
                 )
    edges.append(Edge(source="student 22",
                      target="student 3"
                      )
                 )
    edges.append(Edge(source="student 22",
                      target="student 6"
                      )
                 )
    edges.append(Edge(source="student 22",
                      target="student 8"
                      )
                 )
    edges.append(Edge(source="student 22",
                      target="student 9"
                      )
                 )
    edges.append(Edge(source="student 22",
                      target="student 13"
                      )
                 )
    edges.append(Edge(source="student 22",
                      target="student 15"
                      )
                 )
    edges.append(Edge(source="student 22",
                      target="student 21"
                      )
                 )
    edges.append(Edge(source="student 13",
                      target="student 3"
                      )
                 )
    edges.append(Edge(source="student 13",
                      target="student 4"
                      )
                 )
    edges.append(Edge(source="student 13",
                      target="student 6"
                      )
                 )
    edges.append(Edge(source="student 13",
                      target="student 7"
                      )
                 )
    edges.append(Edge(source="student 13",
                      target="student 8"
                      )
                 )
    edges.append(Edge(source="student 13",
                      target="student 9"
                      )
                 )
    edges.append(Edge(source="student 13",
                      target="student 15"
                      )
                 )
    edges.append(Edge(source="student 13",
                      target="student 18"
                      )
                 )
    edges.append(Edge(source="student 13",
                      target="student 21"
                      )
                 )
    edges.append(Edge(source="student 13",
                      target="student 22"
                      )
                 )
    edges.append(Edge(source="student 14",
                      target="student 2"
                      )
                 )
    edges.append(Edge(source="student 14",
                      target="student 2"
                      )
                 )
    edges.append(Edge(source="student 14",
                      target="student 4"
                      )
                 )
    edges.append(Edge(source="student 14",
                      target="student 6"
                      )
                 )
    edges.append(Edge(source="student 14",
                      target="student 7"
                      )
                 )
    edges.append(Edge(source="student 14",
                      target="student 8"
                      )
                 )
    edges.append(Edge(source="student 14",
                      target="student 9"
                      )
                 )
    edges.append(Edge(source="student 14",
                      target="student 12"
                      )
                 )
    edges.append(Edge(source="student 14",
                      target="student 13"
                      )
                 )
    edges.append(Edge(source="student 14",
                      target="student 15"
                      )
                 )
    edges.append(Edge(source="student 16",
                      target="student 5"
                      )
                 )
    edges.append(Edge(source="student 16",
                      target="student 10"
                      )
                 )
    edges.append(Edge(source="student 16",
                      target="student 10"
                      )
                 )
    edges.append(Edge(source="student 16",
                      target="student 16"
                      )
                 )
    edges.append(Edge(source="student 16",
                      target="student 17"
                      )
                 )
    edges.append(Edge(source="student 16",
                      target="student 18"
                      )
                 )
    edges.append(Edge(source="student 16",
                      target="student 19"
                      )
                 )
    edges.append(Edge(source="student 16",
                      target="student 20"
                      )
                 )

    config = Config(width=1300,
                    height=700,
                    nodeHighlightBehavior=True,
                    highlightOpacity=.5
                    )

    FourthGraph = agraph(nodes=nodes,
                        edges=edges,
                        config=config)


    fourth_select = st.selectbox('Learn more about the study participants:',
                                 options=fourth_classification['Student'].unique(), index=1)

    #st.write(fourth_classification)


    if fourth_select == 'student 1':
        st.subheader('Multilingual: No')
        st.subheader('Assigned Group: Heterogeneous')

        mask = outsideClass['Student'] == fourth_select
        outsideClass = outsideClass[mask]

        outsideClass.replace('1', 'All English')
        outsideClass.replace('2', 'Mostly English')
        outsideClass.replace('3', 'Equal English and Another Language')
        outsideClass.replace('4', 'Mostly Another Language')
        outsideClass.replace('5', 'All Another Language')

        fig1 = px.pie(outsideClass, names='Location', width=200.0,
                      color_discrete_sequence=px.colors.sequential.RdBu, title='Where this student meets people they '
                                                                               'hang out and work with **outside of class**')
        st.plotly_chart(fig1)

        st. write('No data for this student.')

        fig2 = px.pie(outsideClass, names='Language', width=200.0,
                      color_discrete_sequence=px.colors.sequential.RdBu,
                      title='What languages this student speaks when '
                            'they hang out and work with kids **outside'
                            ' of class**')
        st.plotly_chart(fig2)
        st.write('No data for this student.')

    if fourth_select == 'student 3':
        st.subheader('Multilingual: Yes')
        st.subheader('Assigned Group: Heterogeneous')

        mask = outsideClass['Student'] == fourth_select
        outsideClass = outsideClass[mask]


        fig1 = px.pie(outsideClass, names='Location', width=200.0,
                      color_discrete_sequence=px.colors.sequential.RdBu, title='Where this student meets people they '
                                                                               'hang out and work with **outside of class**')
        st.plotly_chart(fig1)

        fig2 = px.pie(outsideClass, names='Language', width=200.0,
                      color_discrete_sequence=px.colors.sequential.RdBu,
                      title='What languages this student speaks when '
                            'they hang out and work with kids **outside'
                            ' of class**')
        st.plotly_chart(fig2)
        st.write('Where 1 = **All English**, 2 = **Mostly English**, 3 = **Equal English and Another Language**, '
                 '4 = **Mostly Another'
                 ' Language**, 5 = **All Another Language**')

    if fourth_select == 'student 13':
        st.subheader('Multilingual: No')
        st.subheader('Assigned Group: Heterogeneous')

        mask = outsideClass['Student'] == fourth_select
        outsideClass = outsideClass[mask]


        fig1 = px.pie(outsideClass, names='Location', width=200.0,
                      color_discrete_sequence=px.colors.sequential.RdBu, title='Where this student meets people they '
                                                                               'hang out and work with **outside of class**')
        st.plotly_chart(fig1)

        fig2 = px.pie(outsideClass, names='Language', width=200.0,
                      color_discrete_sequence=px.colors.sequential.RdBu,
                      title='What languages this student speaks when '
                            'they hang out and work with kids **outside'
                            ' of class**')
        st.plotly_chart(fig2)
        st.write('Where 1 = **All English**, 2 = **Mostly English**, 3 = **Equal English and Another Language**, '
                 '4 = **Mostly Another'
                 ' Language**, 5 = **All Another Language**')

    if fourth_select == 'student 4':
        st.subheader('Multilingual: Yes')
        st.subheader('Assigned Group: Homogeneous')

        mask = outsideClass['Student'] == fourth_select
        outsideClass = outsideClass[mask]


        fig1 = px.pie(outsideClass, names='Location', width=200.0,
                      color_discrete_sequence=px.colors.sequential.RdBu, title='Where this student meets people they '
                                                                               'hang out and work with **outside of class**')
        st.plotly_chart(fig1)

        fig2 = px.pie(outsideClass, names='Language', width=200.0,
                      color_discrete_sequence=px.colors.sequential.RdBu,
                      title='What languages this student speaks when '
                            'they hang out and work with kids **outside'
                            ' of class**')
        st.plotly_chart(fig2)
        st.write('Where 1 = **All English**, 2 = **Mostly English**, 3 = **Equal English and Another Language**, '
                 '4 = **Mostly Another'
                 ' Language**, 5 = **All Another Language**')

    if fourth_select == 'student 8':
        st.subheader('Multilingual: Yes')
        st.subheader('Assigned Group: Homogeneous')

        mask = outsideClass['Student'] == fourth_select
        outsideClass = outsideClass[mask]


        fig1 = px.pie(outsideClass, names='Location', width=200.0,
                      color_discrete_sequence=px.colors.sequential.RdBu, title='Where this student meets people they '
                                                                               'hang out and work with **outside of class**')
        st.plotly_chart(fig1)

        fig2 = px.pie(outsideClass, names='Language', width=200.0,
                      color_discrete_sequence=px.colors.sequential.RdBu,
                      title='What languages this student speaks when '
                            'they hang out and work with kids **outside'
                            ' of class**')
        st.plotly_chart(fig2)
        st.write('Where 1 = **All English**, 2 = **Mostly English**, 3 = **Equal English and Another Language**, '
                 '4 = **Mostly Another'
                 ' Language**, 5 = **All Another Language**')
    if fourth_select == 'student 14':
        st.subheader('Multilingual: Yes')
        st.subheader('Assigned Group: Heterogeneous')

        mask = outsideClass['Student'] == fourth_select
        outsideClass = outsideClass[mask]


        fig1 = px.pie(outsideClass, names='Location', width=200.0,
                      color_discrete_sequence=px.colors.sequential.RdBu, title='Where this student meets people they '
                                                                               'hang out and work with **outside of class**')
        st.plotly_chart(fig1)

        fig2 = px.pie(outsideClass, names='Language', width=200.0,
                      color_discrete_sequence=px.colors.sequential.RdBu,
                      title='What languages this student speaks when '
                            'they hang out and work with kids **outside'
                            ' of class**')
        st.plotly_chart(fig2)
        st.write('Where 1 = **All English**, 2 = **Mostly English**, 3 = **Equal English and Another Language**, '
                 '4 = **Mostly Another'
                 ' Language**, 5 = **All Another Language**')

    if fourth_select == 'student 5':
        st.subheader('Multilingual: Yes')
        st.subheader('Assigned Group: Homogeneous')

        mask = outsideClass['Student'] == fourth_select
        outsideClass = outsideClass[mask]


        fig1 = px.pie(outsideClass, names='Location', width=200.0,
                      color_discrete_sequence=px.colors.sequential.RdBu, title='Where this student meets people they '
                                                                               'hang out and work with **outside of class**')
        st.plotly_chart(fig1)

        fig2 = px.pie(outsideClass, names='Language', width=200.0,
                      color_discrete_sequence=px.colors.sequential.RdBu,
                      title='What languages this student speaks when '
                            'they hang out and work with kids **outside'
                            ' of class**')
        st.plotly_chart(fig2)
        st.write('Where 1 = **All English**, 2 = **Mostly English**, 3 = **Equal English and Another Language**, '
                 '4 = **Mostly Another'
                 ' Language**, 5 = **All Another Language**')

    if fourth_select == 'student 16':
        st.subheader('Multilingual: Yes')
        st.subheader('Assigned Group: Homogeneous')

        mask = outsideClass['Student'] == fourth_select
        outsideClass = outsideClass[mask]


        fig1 = px.pie(outsideClass, names='Location', width=200.0,
                      color_discrete_sequence=px.colors.sequential.RdBu, title='Where this student meets people they '
                                                                               'hang out and work with **outside of class**')
        st.plotly_chart(fig1)

        fig2 = px.pie(outsideClass, names='Language', width=200.0,
                      color_discrete_sequence=px.colors.sequential.RdBu,
                      title='What languages this student speaks when '
                            'they hang out and work with kids **outside'
                            ' of class**')
        st.plotly_chart(fig2)
        st.write('Where 1 = **All English**, 2 = **Mostly English**, 3 = **Equal English and Another Language**, '
                 '4 = **Mostly Another'
                 ' Language**, 5 = **All Another Language**')


    #YesNo = fourth_classification.at['']

    # for selection in fourth_select:
    #     st.subheader(selection)
    #     st.subheader('Classified EL:')
    #     mask1 = fourth_classification.filter('Student'== fourth_select)
    #     fourth_classification = fourth_classification[mask1]
    #     st.write(fourth_classification)
    #     YesNo = fourth_classification.at['EL']
    #     YesNo
    #     #st.write(fourth_classification, names='EL')
    #     st.subheader('Assigned Group: Heterogeneous')

    # mask = outsideClass['Student'== fourth_select]
    # outsideClass = outsideClass[mask]
    #
    # fig1 = px.pie(outsideClass, names='Location', width=200.0,
    #                       color_discrete_sequence=px.colors.sequential.RdBu, title='Where this student meets people they '
    #                                                                                'hang out and work with outside of class')
    # st.plotly_chart(fig1)
    #
    # fig2 = px.pie(outsideClass, names='Language', width=200.0,
    #                   color_discrete_sequence=px.colors.sequential.RdBu, title='What languages this student speaks when '
    #                                                                            'they hang out and work with kids outside'
    #                                                                            ' of class')
    # st.plotly_chart(fig2)

    # if fourth_select == 'student 3':
    #     st.subheader('Classified EL: No')
    #     st.subheader('Assigned Group: Heterogeneous')
    #
    #     mask = outsideClass['Student'] != fourth_select
    #     outsideClass = outsideClass[mask]
    #
    #     fig1 = px.pie(outsideClass, names='Location', width=200.0,
    #                       color_discrete_sequence=px.colors.sequential.RdBu, title='Where this student meets people they '
    #                                                                                'hang out and work with outside of class')
    #     st.plotly_chart(fig1)
    #
    #     fig2 = px.pie(outsideClass, names='Language', width=200.0,
    #                   color_discrete_sequence=px.colors.sequential.RdBu, title='What languages this student speaks when '
    #                                                                            'they hang out and work with kids outside'
    #                                                                            ' of class')
    #     st.plotly_chart(fig2)






