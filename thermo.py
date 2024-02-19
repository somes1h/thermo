import streamlit as st
import matplotlib.pyplot as plt
import numpy as np

def plot_process(process_type, pressure_values, volume_values):
    plt.figure(figsize=(8, 6))

    if process_type == "Isothermal":
        plt.plot(volume_values, pressure_values, label="Isothermal Process", color="b")
    elif process_type == "Isobaric":
        plt.plot(volume_values, pressure_values, label="Isobaric Process", color="r")
    elif process_type == "Isochoric":
        plt.plot(volume_values, pressure_values, label="Isochoric Process", color="g")
    elif process_type == "Adiabatic":
        plt.plot(volume_values, pressure_values, label="Adiabatic Process", color="m")
    else:
        st.error("Invalid process type selected!")
        return

    plt.xlabel("Volume")
    plt.ylabel("Pressure")
    plt.title(f"{process_type} Process")
    plt.legend()
    plt.grid(True)
    plt.savefig('graph.jpg')
    st.image('graph.jpg')
    #st.pyplot()

def main():
    st.title("Thermodynamic Processes Visualization")

    process_type = st.selectbox("Select process type:",
                                ["Isothermal", "Isobaric", "Isochoric", "Adiabatic"])

    pressure_values = st.text_input("Enter pressure values (comma-separated):")
    volume_values = st.text_input("Enter volume values (comma-separated):")

    if st.button("Plot"):
        try:
            pressure_values = [float(p) for p in pressure_values.split(",")]
            volume_values = [float(v) for v in volume_values.split(",")]

            plot_process(process_type, pressure_values, volume_values)
        except ValueError:
            st.error("Please enter valid pressure and volume values!")

if __name__ == "__main__":
    main()
