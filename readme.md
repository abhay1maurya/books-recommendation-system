### **Books Recommendation System**  

This project is a **Book Recommendation System** that recommends books similar to the one provided by the user. It uses a combination of machine learning techniques, Flask for the backend, and an interactive HTML frontend. Additionally, it includes a **requirement testing script** to ensure the environment is properly set up before running the application.

---

### **Features**  
1. **Input a Book Title**: Users can enter the title of a book they like.  
2. **Recommendations**: The system provides a list of similar books based on the input title.  
3. **Interactive Frontend**:  
   - User-friendly interface with responsive design.  
   - Styled recommendation cards for better visualization.  
4. **Machine Learning Backend**:  
   - Implements the **NearestNeighbors algorithm** for finding similar books.  
5. **Requirement Testing Script**:  
   - Ensures all necessary Python libraries are installed before running the application.  

---

### **Technologies Used**  
#### **Frontend**  
- HTML, CSS, Bootstrap for structure and styling.  
- JavaScript for dynamic interaction and results rendering.

#### **Backend**  
- Python with Flask for building the web application.  
- **Pandas** for data manipulation and preprocessing.  
- **scikit-learn** for the NearestNeighbors algorithm.

#### **Dataset**  
The dataset includes various book-related features such as:  
- `title`: Book title.  
- `authors`: Author(s) of the book.  
- `average_rating`: Average user rating.  
- `language_code`: Book language.  
- `ratings_count` and `text_reviews_count`: Popularity metrics.  

Preprocessing was performed to normalize and enhance the data for model performance.

---

### **Setup Instructions**  
1. Clone the repository:  
   ```bash
   git clone https://github.com/your-username/books-recommendation-system.git
   cd books-recommendation-system
   ```
2. Install the required Python packages:  
   ```bash
   pip install -r requirements.txt
   ```
3. Test your environment setup by running the `test_requirements.py` script:  
   ```bash
   python test_requirements.py
   ```
   - This script checks for missing dependencies and provides installation instructions if necessary.
4. Add the `books.csv` dataset file to the project directory.  
5. Run the Flask application:  
   ```bash
   python app.py
   ```
6. Open the application in your browser at:  
   ```
   http://127.0.0.1:5000/
   ```

---

### **Usage**  
1. Enter a book title in the input field (e.g., "The Great Gatsby").  
2. Click the "Get Recommendations" button.  
3. View the recommended books on the frontend.

---

### **Example Output**  
- **Input**: "The Great Gatsby"  
- **Recommendations**:  
  - "To Kill a Mockingbird"  
  - "1984"  
  - "The Catcher in the Rye"  
  - "Pride and Prejudice"

---

### **Files Included**  
1. **`app.py`**: The main Flask application file for backend logic.  
2. **`index.html`**: The frontend HTML file for user interaction.  
3. **`books.csv`**: Dataset containing book details.  
4. **`requirements.txt`**: List of required Python libraries.  
5. **`test_requirements.py`**: A script to verify that all dependencies are installed.

---

### **Requirement Test Script**  
The `test_requirements.py` script ensures that all necessary libraries are installed.  
- To run the script:  
  ```bash
  python test_requirements.py
  ```
- If libraries are missing, it will provide installation instructions.  

---

### **Future Enhancements**  
- Deploy the application online using platforms like Heroku or AWS.  
- Add user accounts and personalized recommendations.  
- Expand dataset to include more books and additional metadata.  
- Integrate advanced filtering options (genres, publication years, etc.).  

---

### **Acknowledgments**  
- Dataset source: [The Clever Programmer](https://thecleverprogrammer.com/2023/10/30/book-recommendation-system-with-python/)  
- Python libraries: Flask, pandas, scikit-learn  

---

### **License**  
This project is licensed under the MIT License.  See the [LICENSE](LICENSE) file for details.

---

### **Contributing**  
Contributions are welcome! Fork the repository, make your changes, and submit a pull request.  

---

Let me know if you'd like further adjustments!
