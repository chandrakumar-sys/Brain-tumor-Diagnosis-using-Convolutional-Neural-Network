import h5py

# Open the H5 file
with h5py.File("C:\project\Brain-Tumor-Classification-master\BrainTumorClassifier.h5") as f:
    # Print the structure of the file
    print(f.keys())
    # Access datasets
    dataset = f['dataset_name']
    # Read data from dataset
    data = dataset[:]
