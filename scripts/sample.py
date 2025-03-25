import time
import numpy as np

MOD=998244353

def score(A):
    return np.sum(A%MOD)

def push_stamp(board, stamp, top_left=(0, 0)):
    """
    A の指定した位置に stamp を重ねて加算する関数（インプレース処理で高速）
    
    Parameters:
        A (np.ndarray): 元の大きな行列
        stamp (np.ndarray): 重ねる小さな行列
        top_left (tuple): stamp を配置する A の左上のインデックス (row, col)
    
    Returns:
        np.ndarray: stamp を A の一部に足した結果の行列
    """
    # B を配置する開始位置
    r, c = top_left
    # A の該当部分に B を加算（インプレースで実行）
    board[r:r+stamp.shape[0], c:c+stamp.shape[1]] += stamp
    return board  # 変更後の A を返す（A 自体も更新される）

def solve(epsilon,cooling_rate,epoch):
    N,M,K=map(int,input().split())

    A=[list(map(int,input().split())) for _ in range(N)]
    A=np.array(A,dtype=np.int64)

    stamps=[]
    for _ in range(M):
        stamp=[]
        for _ in range(3):
            stamp.append(list(map(int,input().split())))
        stamps.append(stamp)
    stamps=np.array(stamps,dtype=np.int64)

    alterA=push_stamp(A.copy(),stamps[0],(1,1))


    return epoch

if __name__ == "__main__":
    solve(0.1,0.1,0.1)