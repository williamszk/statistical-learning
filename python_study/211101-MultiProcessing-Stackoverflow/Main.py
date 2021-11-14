import parallelTestModule

if __name__ == '__main__':    
    extractor = parallelTestModule.ParallelExtractor()
    extractor.runInParallel(numProcesses=2, numThreads=4)