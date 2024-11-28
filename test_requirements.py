import importlib

# List of required libraries
required_libraries = [
    "flask",
    "pandas",
    "scikit-learn"
]

def test_requirements():
    """Test if all required libraries are installed."""
    missing_libraries = []
    for library in required_libraries:
        try:
            importlib.import_module(library)
            print(f"✅ {library} is installed.")
        except ImportError:
            missing_libraries.append(library)
            print(f"❌ {library} is NOT installed.")
    
    if missing_libraries:
        print("\nThe following libraries are missing:")
        for library in missing_libraries:
            print(f"- {library}")
        print("\nPlease install them using:")
        print(f"pip install {' '.join(missing_libraries)}")
    else:
        print("\nAll required libraries are installed. You're good to go!")

if __name__ == "__main__":
    print("Checking requirements for Book Recommendation System...\n")
    test_requirements()
