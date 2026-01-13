def main():
    print("Hello, GCP! This app was deployed via Jenkins.")
    # Simulate creating an artifact (output file)
    with open("build_output.txt", "w") as f:
        f.write("Build Successful: Deployed from jenking aautomate")

if __name__ == "__main__":
    main()
