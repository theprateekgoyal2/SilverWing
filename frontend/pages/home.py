import os
import sys
import streamlit as st
from streamlit_autorefresh import st_autorefresh

from apis import fetch_dishes, toggle_publish

st.set_page_config(page_title="Dishes", layout="wide")
st.title("🍛 All Dishes")

st_autorefresh(interval=10000, key="refresh")

dishes = fetch_dishes()

if not dishes:
    st.warning("No dishes available.")
else:
    cols = st.columns(3)

    for index, dish in enumerate(dishes):
        with cols[index % 3]:
            st.image(dish["image_url"], use_container_width=True)

            # Link to DishDetails page using query param
            dish_id = dish["dish_id"]
            dish_name = dish["dish_name"].title()
            url = f"./dish_details?dish_id={dish_id}"

            st.markdown(f"### [{dish_name}]({url})", unsafe_allow_html=True)

            description = dish.get("description") or "No description available"
            st.caption(description)
            st.write(f'last updated at: {dish.get("last_updated")}')

            publish = dish.get("is_published", False)
            button_text = "Unpublish" if publish else "Publish"
            button_key = f"{dish['dish_id']}-toggle"

            if st.button(button_text, key=button_key):
                toggle_publish(dish['dish_id'], publish)
