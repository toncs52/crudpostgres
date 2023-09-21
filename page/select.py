import sys
import streamlit as st
sys.path.insert(1, 'crudpostgres\controller')
import client as client



def select_all():
    st.title("Select All person")

    rows = client.select_all()
    if rows:
        st.title("Select All Persson")

        rows = client.select_all()

        if rows:
            st.table(rows)
        else:
            st.write(" ยังไม่มีข้อมูลในตาราง")
