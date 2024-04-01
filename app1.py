import streamlit as st
import certifi
import os
from dotenv import load_dotenv
from pymongo import MongoClient
import pandas as pd
import plotly.express as px



# Load environment variables
# load_dotenv()

# MongoDB connection
# mongodb_uri = os.getenv("MONGODB_URI")
# client = MongoClient(mongodb_uri, tlsCAFile=certifi.where())
# db = client["survay"]

# collection = db["users"]

# Streamlit app
st.set_page_config(layout="wide",page_title="Survey",page_icon=":bar_chart:")

st.title(":bar_chart: Political Survey in Jharkhand 2024")
st.markdown('<style>div.block-container{padding-top:1rem;}</style>',unsafe_allow_html=True)

# # Fetch data from MongoDB collection
# documents = list(collection.find({}))

# # Convert ObjectId values to strings in the _id field
# for doc in documents:
#     doc['_id'] = str(doc['_id'])

# # Create DataFrame from modified documents
df = pd.DataFrame([
  {
    "Name": "Aditi Sharma",
    "Number": "9876543310",
    "Age Group": "25-34",
    "Gender": "Female",
    "Occupation": "Private Employee",
    "Constituency": "Ranchi",
    "Interested": "Yes",
    "Additional Comments": "Passionate about education reform."
  },
  {
    "Name": "Rajesh Patel",
    "Number": "9876543311",
    "Age Group": "35-44",
    "Gender": "Male",
    "Occupation": "Government employee",
    "Constituency": "Jamshedpur",
    "Interested": "No",
    "Additional Comments": "Active in local sports community."
  },
  {
    "Name": "Sneha Gupta",
    "Number": "9876543312",
    "Age Group": "45-54",
    "Gender": "Female",
    "Occupation": "Businessman/trader",
    "Constituency": "Singhbhum",
    "Interested": "Yes",
    "Additional Comments": "Advocates for women's rights."
  },
  {
    "Name": "Amit Kumar",
    "Number": "9876543313",
    "Age Group": "55-64",
    "Gender": "Male",
    "Occupation": "Farmer",
    "Constituency": "Khunti",
    "Interested": "Yes",
    "Additional Comments": "Interested in sustainable development."
  },
  {
    "Name": "Neha Sharma",
    "Number": "9876543314",
    "Age Group": "65 or older",
    "Gender": "Female",
    "Occupation": "Private Employee",
    "Constituency": "Lohardaga",
    "Interested": "No",
    "Additional Comments": "Involved in local charity work."
  },
  {
    "Name": "Vivek Singh",
    "Number": "9876543315",
    "Age Group": "18-24",
    "Gender": "Male",
    "Occupation": "Student",
    "Constituency": "Dhanbad",
    "Interested": "Yes",
    "Additional Comments": "Passionate about environmental conservation."
  },
  {
    "Name": "Ananya Verma",
    "Number": "9876543316",
    "Age Group": "25-34",
    "Gender": "Female",
    "Occupation": "Government employee",
    "Constituency": "Chatra",
    "Interested": "No",
    "Additional Comments": "Active in community health initiatives."
  },
  {
    "Name": "Sanjay Gupta",
    "Number": "9876543317",
    "Age Group": "35-44",
    "Gender": "Male",
    "Occupation": "Businessman/trader",
    "Constituency": "Rajmahal",
    "Interested": "Yes",
    "Additional Comments": "Advocates for small business development."
  },
  {
    "Name": "Meera Devi",
    "Number": "9876543318",
    "Age Group": "45-54",
    "Gender": "Female",
    "Occupation": "Private Employee",
    "Constituency": "Dumka",
    "Interested": "Yes",
    "Additional Comments": "Works with local women's cooperative."
  },
  {
    "Name": "Rakesh Singh",
    "Number": "9876543319",
    "Age Group": "55-64",
    "Gender": "Male",
    "Occupation": "Farmer",
    "Constituency": "Godda",
    "Interested": "No",
    "Additional Comments": "Active in local religious community."
  },
  {
    "Name": "Aarav Kumar",
    "Number": "9876543210",
    "Age Group": "18-24",
    "Gender": "Male",
    "Occupation": "Student",
    "Constituency": "Rajmahal",
    "Interested": "Yes",
    "Additional Comments": "Enthusiastic about community service."
  },
  {
    "Name": "Priya Singh",
    "Number": "9876543211",
    "Age Group": "25-34",
    "Gender": "Female",
    "Occupation": "Government employee",
    "Constituency": "Dumka",
    "Interested": "No",
    "Additional Comments": "Interested in environmental issues."
  },
  {
    "Name": "Rohit Patil",
    "Number": "9876543212",
    "Age Group": "35-44",
    "Gender": "Male",
    "Occupation": "Businessman/trader",
    "Constituency": "Godda",
    "Interested": "Yes",
    "Additional Comments": "Looking for business opportunities."
  },
  {
    "Name": "Anjali Rao",
    "Number": "9876543213",
    "Age Group": "45-54",
    "Gender": "Female",
    "Occupation": "Private Employee",
    "Constituency": "Chatra",
    "Interested": "No",
    "Additional Comments": "Volunteers at local NGO."
  },
  {
    "Name": "Manish Gupta",
    "Number": "9876543214",
    "Age Group": "55-64",
    "Gender": "Male",
    "Occupation": "Farmer",
    "Constituency": "Kodarma",
    "Interested": "Yes",
    "Additional Comments": "Advocates for sustainable farming."
  },

  {
    "Name": "Varun Nair",
    "Number": "9876543305",
    "Age Group": "18-24",
    "Gender": "Male",
    "Occupation": "Student",
    "Constituency": "Singhbhum",
    "Interested": "Yes",
    "Additional Comments": "Active in student politics."
  },
  {
    "Name": "Lakshmi Das",
    "Number": "9876543306",
    "Age Group": "25-34",
    "Gender": "Female",
    "Occupation": "Government employee",
    "Constituency": "Khunti",
    "Interested": "No",
    "Additional Comments": "Interested in women's rights."
  },
  {
    "Name": "Suresh Yadav",
    "Number": "9876543307",
    "Age Group": "35-44",
    "Gender": "Male",
    "Occupation": "Businessman/trader",
    "Constituency": "Lohardaga",
    "Interested": "Yes",
    "Additional Comments": "Wants to improve local infrastructure."
  },
  {
    "Name": "Rohan Das",
    "Number": "9876543308",
    "Age Group": "55-64",
    "Gender": "Male",
    "Occupation": "Farmer",
    "Constituency": "Hazaribagh",
    "Interested": "Yes",
    "Additional Comments": "Active in local politics."
  },
  {
    "Name": "Isha Goyal",
    "Number": "9876543309",
    "Age Group": "45-54",
    "Gender": "Female",
    "Occupation": "Businessman/trader",
    "Constituency": "Palamau",
    "Interested": "No",
    "Additional Comments": "Works with women's empowerment groups."
  }
],columns=["Name","Number","Age Group","Gender","Occupation","Constituency","Interested","Additional Comments"])


st.write(df)

col1, col2 = st.columns((2))


st.sidebar.header("Choose your filter: ")
# Create for Constituency
Constituency = st.sidebar.multiselect("Pick your Constituency", df["Constituency"].unique())
if not Constituency:
    df2 = df.copy()
else:
    df2 = df[df["Constituency"].isin(Constituency)]

# Create for Occupation
Occupation = st.sidebar.multiselect("Pick the Occupation", df2["Occupation"].unique())
if not Occupation:
    df3 = df2.copy()
else:
    df3 = df2[df2["Occupation"].isin(Occupation)]

# Create for Age Group"
Age= st.sidebar.multiselect("Pick the Age Group",df3["Age Group"].unique())
if not Age:
    df4=df3.copy()
else:
    df4 = df3[df3["Age Group"].isin(Age)]
# Create for Gender
Gender= st.sidebar.multiselect("Pick the Gender", df4["Gender"].unique())
if not Gender:
    df5=df4.copy()
else:
    df5 = df4[df4["Gender"].isin(Gender)]
# Filter the data based on Constituency, Occupation and Age

if not Constituency and not Occupation and not Age and not Gender:
    filtered_df = df
elif not Occupation and not Age:
    filtered_df = df[df["Constituency"].isin(Constituency)]
elif not Constituency and not Age:
    filtered_df = df[df["Occupation"].isin(Occupation)]
elif Occupation and Age:
    filtered_df = df3[df["Occupation"].isin(Occupation) & df3["Age"].isin(Age)]
elif Constituency and Age:
    filtered_df = df3[df["Constituency"].isin(Constituency) & df3["Age Group"].isin(Age)]
elif Constituency and Occupation:
    filtered_df = df3[df["Constituency"].isin(Constituency) & df3["Occupation"].isin(Occupation)]
elif Age:
    filtered_df = df3[df3["Age Group"].isin(Age)]

else:
    filtered_df = df3[df3["Constituency"].isin(Constituency) & df3["Occupation"].isin(Occupation) & df3["Age Group"].isin(Age)]

if Gender:
    filtered_df = df5


with col1:
    # Group by Constituency and count the number of people in each Constituency
    constituency_counts = filtered_df['Constituency'].value_counts().reset_index()
    constituency_counts.columns = ['Constituency', 'Number of People']

   # Plot the bar chart
    st.subheader("Constituency wise People")
    fig = px.bar(constituency_counts, x="Constituency", y="Number of People", text=constituency_counts['Number of People'],
             template="seaborn",color='Constituency')
    st.plotly_chart(fig, use_container_width=True, height=200)

with col2:
    gender_counts = filtered_df['Gender'].value_counts().reset_index()
    gender_counts.columns = ['Gender', 'Number of People']

    # Plot the pie chart
    st.subheader("Gender wise People")
    fig = px.pie(gender_counts, values="Number of People", names="Gender", hole=0.5)
    fig.update_traces(textinfo='percent+label', textposition='inside', showlegend=False)
    st.plotly_chart(fig, use_container_width=True)

cl1, cl2 = st.columns((2))
with cl1:
    with st.expander("Constituency Data"):
        st.write(filtered_df.style.background_gradient(cmap="Blues"))
        csv = filtered_df.to_csv(index = False).encode('utf-8')
        st.download_button("Download Data", data = csv, file_name = "Constituency_Data.csv", mime = "text/csv",
                            help = 'Click here to download the data as a CSV file')

        

chart1, chart2 = st.columns((2))
with chart1:
    st.subheader('Occupation wise People')
    occupation_counts = filtered_df.groupby('Occupation').size().reset_index(name='Count')

    fig = px.pie(occupation_counts, values='Count', names='Occupation', template='plotly_dark')

    # Update the chart layout
    fig.update_traces(textinfo='percent+label', textposition='inside')

    # Display the chart using Streamlit
    st.plotly_chart(fig, use_container_width=True)

with chart2:
    st.subheader('Interested People in Constituency')
    interested_df = filtered_df[filtered_df['Interested'] == 'Yes']
    constituency_counts = interested_df.groupby('Constituency').size().reset_index(name='Number of People')
    fig = px.bar(constituency_counts, y='Number of People', x='Constituency', text='Number of People',
             template='seaborn',color='Constituency')
    fig.update_traces( textposition = "inside")
    st.plotly_chart(fig,use_container_width=True)


with chart2:
    with st.expander("Constituency Interested Data"):
        st.write(interested_df.style.background_gradient(cmap="Blues"))
        csv = interested_df.to_csv(index = False).encode('utf-8')
        st.download_button("Download Data", data = csv, file_name = "Interested_Constituency_Data.csv", mime = "text/csv",
                            help = 'Click here to download the data as a CSV file')


with st.expander("View Survey Data"):
    st.write(df.style.background_gradient(cmap="Oranges"))

    # Download orginal DataSet
    csv = df.to_csv(index = False).encode('utf-8')
    st.download_button('Download Data', data = csv, file_name = "Data.csv",mime = "text/csv")