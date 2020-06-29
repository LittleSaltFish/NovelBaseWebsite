from numpy import *
from numpy import linalg as la
#玄幻0，言情1，悬疑2，都市3，科幻4，军事5，轻小说6，历史7，政治8,科学9,文学10


def ALL():
    def loadExData2():
        data = [[["玄幻", 2], ["言情", 0], ["悬疑", 0], ["都市", 4], ["科幻", 4], ["军事", 0], ["轻小说", 0], ["历史", 0], ["政治", 0], ["科学", 0], ["文学", 0]],
                [["玄幻", 0], ["言情", 0], ["悬疑", 0], ["都市", 1], ["科幻", 0], ["军事", 0], [
                    "轻小说", 0], ["历史", 0], ["政治", 0], ["科学", 0], ["文学", 5]],
                [["玄幻", 0], ["言情", 0], ["悬疑", 0], ["都市", 0], ["科幻", 0], ["军事", 0], [
                    "轻小说", 0], ["历史", 1], ["政治", 0], ["科学", 4], ["文学", 0]],
                [["玄幻", 3], ["言情", 3], ["悬疑", 4], ["都市", 0], ["科幻", 3], ["军事", 0],
                 ["轻小说", 0], ["历史", 2], ["政治", 2], ["科学", 0], ["文学", 0]],
                [["玄幻", 5], ["言情", 5], ["悬疑", 5], ["都市", 0], ["科幻", 0], ["军事", 0],
                 ["轻小说", 0], ["历史", 0], ["政治", 0], ["科学", 0], ["文学", 0]],
                [["玄幻", 0], ["言情", 0], ["悬疑", 0], ["都市", 0], ["科幻", 0], ["军事", 0],
                 ["轻小说", 5], ["历史", 0], ["政治", 0], ["科学", 5], ["文学", 0]],
                [["玄幻", 4], ["言情", 0], ["悬疑", 4], ["都市", 0], ["科幻", 0], ["军事", 0],
                 ["轻小说", 0], ["历史", 0], ["政治", 0], ["科学", 0], ["文学", 5]],
                [["玄幻", 0], ["言情", 0], ["悬疑", 0], ["都市", 0], ["科幻", 0], ["军事", 4],
                 ["轻小说", 0], ["历史", 0], ["政治", 0], ["科学", 0], ["文学", 4]],
                [["玄幻", 0], ["言情", 0], ["悬疑", 0], ["都市", 0], ["科幻", 0], ["军事", 0],
                 ["轻小说", 5], ["历史", 0], ["政治", 0], ["科学", 5], ["文学", 0]],
                [["玄幻", 0], ["言情", 0], ["悬疑", 0], ["都市", 3], ["科幻", 0], ["军事", 0],
                 ["轻小说", 0], ["历史", 0], ["政治", 4], ["科学", 5], ["文学", 0]],
                [["玄幻", 1], ["言情", 1], ["悬疑", 2], ["都市", 1], ["科幻", 1], ["军事", 2], ["轻小说", 1], ["历史", 0], ["政治", 4], ["科学", 5], ["文学", 0]]]
        dataser = 11*['0']
        dataset = []
        for j in range(11):
            for i in range(11):
                   if data[j][i][0] == "玄幻":
                            dataser[i] = data[j][i][1]
                   elif data[j][i][0] == "言情":
                            dataser[i] = data[j][i][1]
                   elif data[j][i][0] == "悬疑":
                            dataser[i] = data[j][i][1]
                   elif data[j][i][0] == "都市":
                            dataser[i] = data[j][i][1]
                   elif data[j][i][0] == "科幻":
                            dataser[i] = data[j][i][1]
                   elif data[j][i][0] == "军事":
                            dataser[i] = data[j][i][1]
                   elif data[j][i][0] == "轻小说":
                            dataser[i] = data[j][i][1]
                   elif data[j][i][0] == "历史":
                            dataser[i] = data[j][i][1]
                   elif data[j][i][0] == "政治":
                            dataser[i] = data[j][i][1]
                   elif data[j][i][0] == "科学":
                            dataser[i] = data[j][i][1]
                   elif data[j][i][0] == "文学":
                            dataser[i] = data[j][i][1]
            dataset.append(dataser)
            dataser = 11*['0']
        return dataset

    #在 Python 中进行 SVD 分解非常简单，利用 Numpy 模块中的 np.linalg.svd() 函数，
    #比如u,sigma,v = np.linalg.svd(A)，其中 u，v 分别返回矩阵 A 的左右奇异向量，
    #而 sigma 返回的是按从大到小的顺序排列的奇异值

    #if __name__ == '__main__':
     #   u,sigma,vt = la.svd(mat(loadExData2()))
      #  print("奇异值矩阵为:\n",sigma)
      #  #计算总能量的90%
      #  sig2 = sigma**2
      #  parSig = sum(sig2)*0.9
      #  print("90%的能量为：\n",parSig)
      #  energy = 0.0
      #  while(energy < parSig):
      #      i = int(input("请输入所需奇异值个数："))
      #      energy = sum(sig2[:i])
      #      print("%d个元素所包含的能量为%f"%(i,energy))

    """
    函数说明：基于SVD的评分估计
    parameters:
        dataMat -数据矩阵
        user -用户编号
        simMeas -相似度计算方法
        item -物品编号
    return:
        物品的估计评分
    """
    def svdEst(dataMat, user, simMeas, item):
        n = shape(dataMat)[1]  # 获取物品个数
        simTotal = 0.0
        ratSimTotal = 0.0
        u, sigma, vt = la.svd(dataMat)  # 对数据矩阵奇异值分解
        sig4 = mat(eye(4)*sigma[:4])  # 只利用包含了90%能量值的奇异值
        xformedItems = dataMat.T * u[:, :4] * sig4.I  # 利用u矩阵将物品转换到低维空间
        for j in range(n):
            userRating = dataMat[user, j]  # 得到用户对该物品的评分
            if userRating == 0 or j == item:
                continue  # 如果评分为0或者物品与比较物品相同，则跳过
            similarity = simMeas(
                xformedItems[item, :].T, xformedItems[j, :].T)  # 转换为列向量，并计算相似度
            print("同一种人对小说类型%d和小说类型%d的喜爱相似度为%f" % (item, j, similarity))
            simTotal += similarity
            ratSimTotal += similarity*userRating
        if simTotal == 0:
            return 0
        else:
            return ratSimTotal/simTotal
        """
    函数说明：给定相似度计算方式，评估物品得分
    parameters:
        dataMat -数据矩阵
        user -用户编号
        simMeas -相似度计算方法引用
        item -物品编号
    return:
        用户对该物品的预估评分
    """
    #对未看的物品进行评分估计
    def standEst(dataMat, user, simMeas, item):
        n = shape(dataMat)[1]  # 行为用户，列为物品。得到物品个数
        simTotal = 0.0
        ratSimTotal = 0.0
        for j in range(n):
            userRating = dataMat[user, j]  # 记录用户对物品j的评分
            if userRating == 0:
                continue  # 用户未对该物品评分，继续
            overLap = nonzero(logical_and(dataMat[:, item].A > 0, dataMat[:, j].A > 0))[
                0]  # 判断重合元素
            #按照不同人的列的评分进行相似度匹配
            #print(dataMat[:,item].A)
            #print(logical_and(dataMat[:,item].A>0,dataMat[:,j].A>0))
            #print(nonzero(logical_and(dataMat[:,item].A>0,dataMat[:,j].A>0)))
            if len(overLap) == 0:
                similarity = 0  # 两个物品没有重合元素，相似度为0
            else:
                # cosSim对重合元素进行相似度计算
                similarity = simMeas(
                    dataMat[overLap, item], dataMat[overLap, j])
            print("同一种人对小说类型%d和小说类型%d的喜爱相似度为%f" % (item, j, similarity))
            simTotal += similarity  # 评分总和
            ratSimTotal += similarity*userRating  # 相似度和当前用户评分的乘积
        if simTotal == 0:
            return 0.0
        else:
            return ratSimTotal/simTotal  # 对数据归一，使得评分值在0-5之间

    """
    函数说明：相似度计算函数(余弦相似度)
    parameters：
        inA -列向量A
        inB -列向量B
    return：
        两个向量的相似度
    """
    def cosSim(inA, inB):
        num = float(inA.T*inB)  # 计算分子
        denom = la.norm(inA)*la.norm(inB)  # 计算分母
        return 0.5+0.5*(num/denom)  # 归一化

    """
    函数说明：推荐函数
    parameters:
        dataMat -数据矩阵
        user -用户编号
        N -产生推荐结果的个数
        simMeas -相似度计算方法
        estMethod -评估函数
    return:
        返回N个推荐结果
    """
    def recommend(dataMat, user, N=3, simMeas=cosSim, estMethod=standEst):
        unratedItems = nonzero(dataMat[user, :].A == 0)[1]  # 找到该用户还未评分的物品
        if len(unratedItems) == 0:
            return "阅读量过多"
        itemScores = []
        for item in unratedItems:
            estimatedScore = estMethod(
                dataMat, user, simMeas, item)  # 计算该物品的预估得分
            if item == 0:
                name = "玄幻"
            elif item == 1:
                name = "言情"
            elif item == 2:
                name = "悬疑"
            elif item == 3:
                name = "都市"
            elif item == 4:
                name = "科幻"
            elif item == 5:
                name = "军事"
            elif item == 6:
                  name = "轻小说"
            elif item == 7:
                name = "历史"
            elif item == 8:
                 name = "政治"
            elif item == 9:
                   name = "科学"
            elif item == 10:
                   name = "文学"
            itemScores.append((name, estimatedScore))  # 存储到list
            #itemScores.append((item,estimatedScore))    #存储到list
        # 将得分排序，返回前N个
        return sorted(itemScores, key=lambda jj: jj[1], reverse=True)[:N]

    """
    函数说明：相似度计算函数(欧氏距离)
    parameters：
        inA -列向量A
        inB -列向量B
    return：
        两个向量的相似度
    """
    def ecludSim(inA, inB):
        return 1.0/(1.0+la.norm(inA-inB))
    """
    函数说明：相似度计算函数(皮尔逊相关系数)
    parameters：
        inA -列向量A
        inB -列向量B
    return：
        两个向量的相似度
    """
    def pearsSim(inA, inB):
        if len(inA) < 3:
            return 1.0  # 是否存在三个或更多的点。两个向量是完全相关的，返回1
        #print(corrcoef(inA,inB,rowvar=0))
        return 0.5+0.5*corrcoef(inA, inB, rowvar=0)[0][1]  # 将数据归一化到0到1之间
    myMat1 = mat(loadExData2())
    print("使用svdEst,cosSim的推荐结果：\n", recommend(myMat1, 1, estMethod=svdEst))
    print("使用svdEst,pearsSim的推荐结果：\n", recommend(
        myMat1, 1, estMethod=svdEst, simMeas=pearsSim))
    print("使用standEst,pearsSim的推荐结果：\n", recommend(myMat1, 1, simMeas=pearsSim))
    return
