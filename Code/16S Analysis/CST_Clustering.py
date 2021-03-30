import pandas as pds
import numpy as np
import matplotlib.pyplot as plt

from scipy.spatial import distance
from scipy.cluster import hierarchy
from matplotlib.colors import ListedColormap
import seaborn as sns
from sklearn.metrics import silhouette_score, silhouette_samples, davies_bouldin_score 


def cluster16SMatrix(dataMatrix, distanceMetric='jensenshannon', clusterMethod='ward', nClusters=5):
    """
    Function to perform hierarchical clustering of the 16S data matrix. 
    :param pandas.DataFrame dataMatrix: 
    :param distanceMetric: distance metric
    :param clusterMethod:
    :param nClusters:
    :param saveClusterFreqs:
    :return:
    """
    # Cluster the data matrix using the desired metrics
    distanceCalc = distance.pdist(dataMatrix.values, distanceMetric)
    distanceCalc[np.isnan(distanceCalc)] = 0
    colLinkage = hierarchy.linkage(distanceCalc, method=clusterMethod)

    cstCut = hierarchy.cut_tree(colLinkage, nClusters).squeeze()

    cstCut = pds.Series(cstCut)

    clustIdx = [(x, np.where(cstCut == x)[0]) for x in np.unique(cstCut)] 
    
    cstSummary = list()
    for samps in clustIdx:
        currCst = dataMatrix.iloc[samps[1], :]
        freq = currCst.T/currCst.sum(1)
        meanFreq = freq.mean(1)
        sortByMean = np.argsort(meanFreq)
        cstMean = meanFreq.sort_values(ascending=False)
        cstStDev = freq.std(1)[sortByMean[::-1]]
        cstSummary.append([samps[0], cstMean, cstStDev])
    
    distMat = distance.squareform(distanceCalc)
    silhouetteScore = silhouette_score(distMat, cstCut, metric='precomputed')
    silhouetteSamples = silhouette_samples(distMat, cstCut, metric='precomputed')

    return {'clusterID': cstCut, 'SilhouetteScore': silhouetteScore, 'SilhouetteSamples': silhouetteSamples,
            'DistanceMetric': distanceMetric, 'Method': clusterMethod,
            'LinkageMatrix': colLinkage, 'Dendrogram': hierarchy.dendrogram(colLinkage, no_plot=True),
            'ClusterAbundances': cstSummary}


def validateClusters(dataMatrix, distanceMetric='jensenshannon', clusterMethod='ward', method='silhouette', maxClusters=25):
    """
    Function to assess the "optimal" number of clusters for hierarchical clustering.
    :param dataMatrix: 16s data matrix
    :param distanceMetric: distance metric to use in HCA.
    :param clusterMethod: Hierarchical clustering algorithm
    :param method: Select the score metric to optimize. Allowed options are 'silhouette' or 'DBI'.
    :param maxClusters: Maximum number of clusters to examine. Solutions range(2, maxClusters)
    :return: 
    """
    distanceCalc = distance.pdist(dataMatrix.values, distanceMetric)
    distanceCalc[np.isnan(distanceCalc)] = 0
    colLinkage = hierarchy.linkage(distanceCalc, method=clusterMethod)
    distMat = distance.squareform(distanceCalc)

    xAxis = range(2, maxClusters)

    if method == 'silhouette':
        validationValues = [silhouette_score(distMat, hierarchy.cut_tree(colLinkage, x).squeeze(), metric='precomputed') for x in xAxis]
    elif method == 'DBI':
        validationValues = [davies_bouldin_score(dataMatrix, hierarchy.cut_tree(colLinkage, x).squeeze()) for x in xAxis]

    return xAxis, validationValues, method
