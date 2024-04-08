import streamlit as st
import pandas as pd
import joblib

# Load the saved model
model = joblib.load('customer_conversion_rf.joblib')

# Define the encoded values for categorical columns
channelGrouping_mapping = {0.523412: "Paid Search",
                           0.472531: "Display", 0.443895: "(Other)"}
device_browser_mapping = {0.546475: "GoogleAnalytics", 0.173871: "Chrome", 0.307222: "Safari", 0.295620: "Samsung Internet",
                          0.238095: "Firefox", 0.408257: "Edge", 0.195290: "Android Webview", 0.449969: "Opera",
                          0.580077: "Apache-HttpClient"}
device_operatingSystem_mapping = {0.742573: "iOS", 0.176943: "Android", 0.143885: "Windows", 0.254098: "Macintosh",
                                  0.232532: "Chrome OS", 0.378155: "Linux", 0.580077: "(not set)"}
geoNetwork_region_mapping = {0.497873: "Dubai", 0.576437: "Abu Dhabi", 0.481702: "Sharjah", 0.358191: "Ajman",
                             0.450693: "Ras al Khaimah", 0.748268: "(not set)", 0.166667: "England",
                             0.850649: "Umm Al Quawain", 0.895518: "Hessen", 0.000095: "Stockholm County",
                             0.035763: "Cairo Governorate", 0.656838: "Lombardy", 0.995649: "Fujairah",
                             0.032811: "Central Luzon", 0.016705: "Amman Governorate", 0.977106: "Telangana",
                             0.244604: "Metro Manila", 0.742617: "Maharashtra", 0.879443: "Riyadh Province",
                             0.129183: "Ismailia Governorate", 0.850341: "New York", 0.806274: "Centre-Val de Loire",
                             0.666929: "Pays de la Loire", 0.220128: "Tel Aviv District", 0.437370: "Normandy",
                             0.378155: "Ontario", 0.758635: "Ile-de-France", 0.582329: "Illinois",
                             0.297142: "Istanbul", 0.710996: "Islamabad Capital Territory", 0.309683: "South Holland",
                             0.443895: "Muscat Governorate", 0.359289: "Shanghai", 0.345633: "County Dublin",
                             0.677446: "Tamil Nadu", 0.356903: "Goa", 0.598360: "Flanders", 0.367753: "Beirut Governorate",
                             0.512625: "Vienna", 0.422907: "Sindh", 0.647096: "Kerala", 0.591835: "Karnataka",
                             0.600076: "North Holland", 0.397535: "Capital Governorate", 0.430378: "North Rhine-Westphalia",
                             0.472374: "Davao Region", 0.449969: "Mount Lebanon Governorate", 0.406489: "Ash Sharqia Governorate",
                             0.620654: "West Bengal", 0.580077: "Federal Territory of Kuala Lumpur", 0.447915: "Washington",
                             0.612762: "Madhya Pradesh", 0.459392: "Assam", 0.585746: "Porto District"}

# Define the minimum and maximum values for numerical columns
numerical_column_ranges = {
    'count_session': (1.0, 270.0),
    'totals_newVisits': (0.0, 1.0),
    'avg_session_time': (2.0, 5441.0),
    'avg_session_time_page': (0.0, 5441.0),
    'single_page_rate': (0.0, 1.0),
    'avg_visit_time': (0.0, 23.0),
    'days_since_first_visit': (0.0, 30.0),
    'visits_per_day': (0.923077, 2397.333),
    'bounce_rate': (0.0, 4.67),
    'bounces': (0.0, 14.0),
    'time_on_site': (0.0, 1250267.0)
}

# Function to map encoded values back to original categories


def map_encoded_value(value, mapping):
    for k, v in mapping.items():
        if value == k:
            return v
    return None

# Function to make predictions


def predict_conversion(data):
    prediction = model.predict(data)
    return prediction

# Define the Streamlit app


# Define the Streamlit app
def main():
    st.title('Conversion Prediction App')
    st.write('Enter the session data to predict conversion:')

    # Input form for user to input data
    count_session = st.number_input('Count Session', min_value=numerical_column_ranges['count_session'][0],
                                    max_value=numerical_column_ranges['count_session'][1])
    channelGrouping = st.selectbox(
        'Channel Grouping', options=list(channelGrouping_mapping.values()))
    device_browser = st.selectbox(
        'Device Browser', options=list(device_browser_mapping.values()))
    device_operatingSystem = st.selectbox('Device Operating System', options=list(
        device_operatingSystem_mapping.values()))
    geoNetwork_region = st.selectbox(
        'GeoNetwork Region', options=list(geoNetwork_region_mapping.values()))
    totals_newVisits = st.number_input('Totals New Visits', min_value=numerical_column_ranges['totals_newVisits'][0],
                                       max_value=numerical_column_ranges['totals_newVisits'][1])
    avg_session_time = st.slider('Average Session Time',
                                 min_value=numerical_column_ranges['avg_session_time'][0],
                                 max_value=numerical_column_ranges['avg_session_time'][1],
                                 step=1.0)
    avg_session_time_page = st.slider('Average Session Time Page',
                                      min_value=numerical_column_ranges['avg_session_time_page'][0],
                                      max_value=numerical_column_ranges['avg_session_time_page'][1],
                                      step=1.0)
    single_page_rate = st.slider('Single Page Rate',
                                 min_value=numerical_column_ranges['single_page_rate'][0],
                                 max_value=numerical_column_ranges['single_page_rate'][1],
                                 step=0.01)
    avg_visit_time = st.slider('Average Visit Time',
                               min_value=numerical_column_ranges['avg_visit_time'][0],
                               max_value=numerical_column_ranges['avg_visit_time'][1],
                               step=1.0)
    days_since_first_visit = st.slider('Days Since First Visit',
                                       min_value=numerical_column_ranges['days_since_first_visit'][0],
                                       max_value=numerical_column_ranges['days_since_first_visit'][1],
                                       step=1.0)
    visits_per_day = st.slider('Visits Per Day',
                               min_value=numerical_column_ranges['visits_per_day'][0],
                               max_value=numerical_column_ranges['visits_per_day'][1],
                               step=1.0)
    bounce_rate = st.slider('Bounce Rate',
                            min_value=numerical_column_ranges['bounce_rate'][0],
                            max_value=numerical_column_ranges['bounce_rate'][1],
                            step=0.01)
    bounces = st.slider('Bounces',
                        min_value=numerical_column_ranges['bounces'][0],
                        max_value=numerical_column_ranges['bounces'][1],
                        step=1.0)
    time_on_site = st.slider('Time on Site',
                             min_value=numerical_column_ranges['time_on_site'][0],
                             max_value=numerical_column_ranges['time_on_site'][1],
                             step=1000.0)

    # Map encoded values back to original categories
    channelGrouping_encoded = [
        k for k, v in channelGrouping_mapping.items() if v == channelGrouping][0]
    device_browser_encoded = [
        k for k, v in device_browser_mapping.items() if v == device_browser][0]
    device_operatingSystem_encoded = [
        k for k, v in device_operatingSystem_mapping.items() if v == device_operatingSystem][0]
    geoNetwork_region_encoded = [
        k for k, v in geoNetwork_region_mapping.items() if v == geoNetwork_region][0]

    # Prepare data for prediction
    data = {
        'count_session': count_session,
        'channelGrouping': channelGrouping_encoded,
        'totals_newVisits': totals_newVisits,
        'device_browser': device_browser_encoded,
        'device_operatingSystem': device_operatingSystem_encoded,
        'geoNetwork_region': geoNetwork_region_encoded,
        'avg_session_time': avg_session_time,
        'avg_session_time_page': avg_session_time_page,
        'single_page_rate': single_page_rate,
        'avg_visit_time': avg_visit_time,
        'days_since_first_visit': days_since_first_visit,
        'visits_per_day': visits_per_day,
        'bounce_rate': bounce_rate,
        'bounces': bounces,
        'time_on_site': time_on_site
    }
    df = pd.DataFrame([data])

    if st.button('Predict'):
        prediction = predict_conversion(df)
        prediction_label = 'Converted' if prediction[0] == 1 else 'Not Converted'
        if prediction_label == 'Converted':
            st.markdown(
                f'<div style="background-color:#32CD32;padding:10px;border-radius:5px;color:white;">Prediction: {prediction_label}</div>', unsafe_allow_html=True)
            st.balloons()
        else:
            st.markdown(
                f'<div style="background-color:#FF5733;padding:10px;border-radius:5px;color:white;">Prediction: {prediction_label}</div>', unsafe_allow_html=True)


if __name__ == "__main__":
    main()
