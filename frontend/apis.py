import requests
import streamlit as st
from constants import API_BASE_URL


def fetch_dishes():
    try:
        response = requests.get(f"{API_BASE_URL}/api/nosh/v1/dishes")
        if response.status_code == 200:
            return response.json().get("dishes", [])
        return []
    except Exception as e:
        st.error(f"Error fetching dishes: {e}")
        return []


def fetch_single_dish(dish_id):
    try:
        response = requests.get(f"{API_BASE_URL}/api/nosh/v1/dishes?dish_id={dish_id}")
        if response.status_code == 200:
            return response.json().get("dish", {})
        return {}
    except Exception as e:
        st.error(f"Error fetching dishes: {e}")
        return []


def toggle_publish(dish_id, current_status: bool):
    try:
        response = requests.post(
            f"{API_BASE_URL}/api/nosh/v1/dishes/toggle?dish_id={dish_id}",
            json={"status": not current_status}
        )
        if response.ok:
            st.success("Status updated!")
        else:
            st.error("Failed to update status")
    except Exception as e:
        st.error(f"Error: {e}")
