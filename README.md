# Cat_or_Not 🐾

A simple web application to classify images as 'cat' or 'not cat' using a pre-trained deep learning model.

![Version](https://img.shields.io/badge/version-1.0.0-blue)
![License](https://img.shields.io/badge/license-None-lightgrey)
![Stars](https://img.shields.io/github/stars/Debkumar-Baksi/Cat_or_Not?style=social)
![Forks](https://img.shields.io/github/forks/Debkumar-Baksi/Cat_or_Not?style=social)

![Project Preview](/preview_example.png)


## ✨ Features

*   🖼️ **Intuitive Web Interface**: Easily upload images for classification through a user-friendly web application built with HTML and Python.
*   🧠 **Deep Learning Classification**: Utilizes a pre-trained deep learning model (`cat_model.h5`) for accurate 'cat' or 'not cat' predictions.
*   🐍 **Python-Powered Backend**: Robust backend developed in Python, handling image processing and model inference efficiently.
*   🛠️ **Utility Scripts**: Includes helper scripts for managing uploaded files (`delete_file.py`) and tracking image counts (`img_counter.py`).
*   🚀 **Quick Setup**: Simple installation process with all dependencies managed via `requirements.txt`.


## ⚙️ Installation Guide

Follow these steps to get the Cat_or_Not application up and running on your local machine.

### Prerequisites

Ensure you have Python 3.8+ installed on your system.

### Step-by-Step Installation

1.  **Clone the Repository**
    Start by cloning the project repository to your local machine:

    ```bash
    git clone https://github.com/Debkumar-Baksi/Cat_or_Not.git
    cd Cat_or_Not
    ```

2.  **Create a Virtual Environment**
    It's recommended to use a virtual environment to manage project dependencies:

    ```bash
    python -m venv venv
    ```

3.  **Activate the Virtual Environment**
    *   **On Windows:**
        ```bash
        .\venv\Scripts\activate
        ```
    *   **On macOS/Linux:**
        ```bash
        source venv/bin/activate
        ```

4.  **Install Dependencies**
    Install all required Python packages using `pip`:

    ```bash
    pip install -r requirements.txt
    ```

5.  **Run the Application**
    Once all dependencies are installed, you can start the Flask web application:

    ```bash
    python app.py
    ```

    The application will typically run on `http://127.0.0.1:5000/`.


## 🚀 Usage Examples

After successfully installing and running the application, navigate to the provided URL in your web browser.

1.  **Open the Application**:
    Open your web browser and go to `http://127.0.0.1:5000/`.

2.  **Upload an Image**:
    You will see an interface to upload an image file. Click the "Choose File" button and select an image from your local machine.

3.  **Get Classification**:
    After selecting an image, click the "Upload & Classify" button (or similar). The application will process the image using the `cat_model.h5` and display whether the image contains a "cat" or "not cat".

![Application Usage Screenshot]([placeholder])
*A screenshot showing the web interface for image upload and classification result.*


## 🗺️ Project Roadmap

The following features and improvements are planned for future versions of Cat_or_Not:

*   **Improved Model Accuracy**: Explore and integrate more advanced pre-trained models or fine-tune the existing one for higher classification accuracy.
*   **Support for More Categories**: Extend the classification capabilities to identify other animals or objects beyond just "cat" or "not cat".
*   **User Feedback Mechanism**: Implement a system for users to provide feedback on classification results, helping to improve the model over time.
*   **Dockerization**: Provide Docker support for easier deployment and environment management.
*   **Enhanced UI/UX**: Refine the user interface for a more modern and responsive experience.


## 🤝 Contribution Guidelines

We welcome contributions to the Cat_or_Not project! Please follow these guidelines to ensure a smooth collaboration:

### Code Style

*   All Python code should adhere to [PEP 8](https://www.python.org/dev/peps/pep-0008/) style guidelines.
*   Maintain consistent formatting throughout the codebase.

### Branch Naming Conventions

*   **Features**: `feature/your-feature-name` (e.g., `feature/add-dog-classifier`)
*   **Bug Fixes**: `bugfix/issue-description` (e.g., `bugfix/upload-error`)
*   **Refactoring**: `refactor/component-name` (e.g., `refactor/model-loading`)

### Pull Request Process

1.  **Fork** the repository.
2.  **Create a new branch** from `main` (or `master`) with an appropriate name.
3.  **Implement your changes** and ensure they are well-tested.
4.  **Commit your changes** with clear and concise commit messages.
5.  **Push your branch** to your forked repository.
6.  **Open a Pull Request** against the `main` branch of the original repository.
    *   Provide a clear title and detailed description of your changes.
    *   Reference any related issues.

### Testing Requirements

*   Ensure all new features include relevant unit or integration tests.
*   Existing tests should pass without errors.


## 📄 License Information

This project is currently released without a formal license. This means that by default, all rights are reserved by the copyright holder, Debkumar-Baksi. You may not distribute, modify, or use this software for commercial purposes without explicit permission.

**Copyright (c) 2023 Debkumar-Baksi**
