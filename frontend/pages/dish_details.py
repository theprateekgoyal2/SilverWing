import streamlit as st
from streamlit_autorefresh import st_autorefresh
from apis import fetch_single_dish, toggle_publish

st.set_page_config(page_title="Dish Details", layout="centered")
st_autorefresh(interval=10000, key="refresh")

dish_id = st.query_params.get("dish_id")

if not dish_id:
    st.error("No dish selected.")
else:
    dish = fetch_single_dish(int(dish_id))

    if not dish:
        st.error("Dish not found.")
    else:
        st.title(dish['dish_name'].title())
        st.image(dish["image_url"], use_container_width=True)
        st.write(f"**Description:** {dish.get('description') or 'No description'}")

        publish = dish.get("is_published", False)
        button_text = "Unpublish" if publish else "Publish"
        button_key = f"{dish['dish_id']}-toggle"

        if st.button(button_text, key=button_key):
            toggle_publish(dish['dish_id'], publish)
