import speedtest
def test_internet_speed():
    st = speedtest.Speedtest()

    print("Измерение скорости загрузки...")
    download_speed = st.download() / 1_000_000  # в мегабитах в секунду
    print(f"Скорость загрузки: {download_speed:.2f} Mbps")

    print("\nИзмерение скорости отдачи...")
    upload_speed = st.upload() / 1_000_000  # в мегабитах в секунду
    print(f"Скорость отдачи: {upload_speed:.2f} Mbps")


if __name__ == "__main__":
    test_internet_speed()
