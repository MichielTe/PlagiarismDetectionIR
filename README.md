# PlagiarismDetectionIR
 This is a project that implements locality sensitive hashing.  
 The values are preset for the data sets in the data directory, but all variables can be changed when needed.
 
 Created by Michiel Téblick and Thibaut Van Goethem for the Information retrieval course at the University of Antwerp  
## Running the project
 This project is build with python 3 using mathplotlib, pickle and hashlib

  The project is build in a "modular" way. With this I mean that each file is a segment on itself, and each file will dump the results of that segment to the obj folder
  
  __It is possible that you still have to create the obj folder__
  
  - The LSH algorithm itself can be run by running preprocessing.py > shingles.py > signatureMatrix.py > LSH.py > postprocessFilter.py in this order
  
    Or you can also run the LSHmain.py which combines all the above except the postprocessfilter.
  
  - There is a LSHquery file that can be run to test your values against a given dataset. This file needs the output from all steps of the process, except the postprocess step.
  This file will plot the result using mathplotlib.
  
  - Jaccard similarity analysis can be done by running the similaritJaccard.py or the similarityApproxyJaccard.py files. The first one needs the data of shingles.py, the second one needs the data of signatureMatrix.py.
  This data can then be plotted using the similarityGraph.py file, which uses mathplotlib.
   
   
   