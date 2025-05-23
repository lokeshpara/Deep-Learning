# MNIST Digit Recognition Web Application

A web application for recognizing handwritten digits using Convolutional Neural Networks (CNN) with different regularization techniques.

## Features

- Interactive digit recognition through drawing or image upload
- Multiple model variants with different regularization techniques:
  - Base Model (No Regularization)
  - L1 Regularization
  - L2 Regularization
  - L1 + L2 Regularization (Best Performance)
- Model performance comparison
- Educational resources about CNN implementation
- Visualization of training progress and misclassified examples

## Model Performance

| Model Type | Test Accuracy | Training Time | Parameters |
|------------|---------------|---------------|------------|
| Base Model | 97.8% | 2.5 min | 1.2M |
| L1 Regularization | 98.2% | 2.8 min | 1.1M |
| L2 Regularization | 98.5% | 2.7 min | 1.2M |
| L1 + L2 Regularization | 98.7% | 3.0 min | 1.1M |

## Setup Instructions

1. Clone the repository:
```bash
git clone https://github.com/lokeshpara/MNIST.git
cd MNIST
```

2. Create and activate a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Run the application:
```bash
python mnist_app/app.py
```

5. Open your browser and navigate to `http://localhost:5000`

## Project Structure

```
mnist_app/
├── static/
│   ├── css/
│   │   └── style.css
│   └── images/
│       ├── training_accuracy_loss.png
│       ├── test_accuracy_loss.png
│       └── misclassified_*.png
├── templates/
│   ├── index.html
│   ├── app.html
│   └── learn.html
├── models/
│   ├── mnist_model.pth
│   ├── mnist_model_l1.pth
│   ├── mnist_model_l2.pth
│   └── mnist_model_l1_l2.pth
└── app.py
```

## Technologies Used

- Python
- Flask
- PyTorch
- HTML/CSS
- JavaScript

## License

This project is licensed under the MIT License - see the LICENSE file for details. 