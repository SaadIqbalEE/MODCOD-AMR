---

# MODCOD Implementation and AMR Development

This repository contains the development, simulation, and implementation of adaptive modulation and coding (MODCOD) schemes, along with a classifier algorithm for automated modulation recognition (AMR) using neural networks (NN). The milestones outline the step-by-step progression of the project.  

---

## Milestone #2: Development and Simulation of Classifier Algorithm  

### Objectives:  
- **Development and Simulation of Classifier Algorithm using NN**:  
  - Formulation of a data packet library for MODCOD implementation, supporting:  
    - Modulation Schemes: M-PSK and M-APSK, where \(M = 2, 4, 8, 16, 32\).  
    - Coding Schemes: Turbo Codes (TC), LDPC, or Polar Codes at various code rates (\(1/4, 1/3, 1/2, 3/4, 5/7, 7/8\), etc.).  
  - Preparation of datasets for training the neural network.  
  - Implementation of the classifier algorithm based on NN.  
  - Simulation of the proposed classifier algorithm in supporting software.  

---

## Milestone #3: MODCOD Implementation on SDR  

### Objectives:  
1. Implementation of MODCOD schemes on Software-Defined Radio (SDR).  
2. Integration of the developed classifier algorithm with SDR for real-time operation.  

---

## Milestone #4: Real-Time Signal Processing and Evaluation  

### Objectives:  
1. Testing the **pre-trained model#10a** (developed during Milestone #3) using an I-Q stream fetched from the receiver USRP.  
2. Designing and implementing an algorithm for real-time signal processing to support the prediction model.  
3. Developing a graphical user interface (GUI) for smooth interaction with the AMR system.  
4. Evaluating the performance of the indigenous AMR system, including a demo video showcasing its working sequence.  

---

## Getting Started  

### Prerequisites:  
- Python and supporting libraries for NN development and simulation.  
- SDR hardware and supporting software (e.g., GNU Radio, MATLAB/Simulink).  
- Neural network training framework (e.g., TensorFlow, PyTorch).  

### Usage:  
1. Clone the repository:  
   '''bash  
   git clone https://github.com/SaadIqbalEE/MODCOD-AMR.git  
   cd MODCOD-AMR 
   '''  
2. Navigate to the milestone-specific directory and follow the setup instructions.  

---

## Repository Structure  

- **Milestone#2**:  
  - Data library formulation scripts and NN training datasets.  
  - Classifier algorithm development and simulation files.  
- **Milestone#3**:  
  - MODCOD implementation scripts for SDR.  
  - Integration files for NN-based classifier.  
- **Milestone#4**:  
  - Real-time signal processing scripts.  
  - GUI source code.  
  - Demo and performance evaluation resources.  

---

## Contributions  
Contributions, feedback, and suggestions are welcome! Open an issue or submit a pull request for improvements or bug fixes.  

---

## License  
This project is licensed under the MIT License. See the 'LICENSE' file for more details.  

---