■[中文](#一筆畫遊戲解法器)    ■[English](#oneline-game-solver)

# **一筆畫遊戲解法器**

## **概述**
給定一張 2D 網格地圖與起點座標，以**單一連續路徑**遍歷所有可走格子，且**每格僅能經過一次**。本專案透過 DFS 回溯搜尋求解此路徑。

- **地圖表示**：二維 list
  - `0`：可走格
  - `-1`：牆
  - `1`：起點（僅限一個）
- **搜尋策略**：DFS 回溯，每步優先展開「可行走鄰格數最少」的節點（Warnsdorff's rule 啟發式），降低無效分支比例
- **剪枝機制**：`checkDead()` 於每步後檢查地圖是否出現不可達格（周圍無可走鄰格），提前終止該分支以避免無謂搜尋

## **安裝**
- **執行環境**：Python 3.x
- **相依套件**：無，僅使用標準庫

```bash
git clone https://github.com/294Ryan/OneLine-Game-solver.git
```

## **使用方式**
1. 於 `OneLine_game_solver_v5_0.py` 開頭修改 `_map` 變數以定義目標地圖
2. 執行：
   ```bash
   python OneLine_game_solver_v5_0.py
   ```
3. 輸出：
   - 地圖視覺化：`▓` 為牆、`▢` 為可走格
   - 有解時：輸出各格對應的**走訪順序編號**（1 為起點）
   - 無解時：輸出 `The map has no way to finish.`

## **常見問題**
- **執行時間過長**
  時間複雜度於最壞情況下呈指數成長，隨地圖規模增加而顯著上升。程式每執行 10 萬次 DFS 呼叫會輸出一次進度（`DFS in N times.`），可用於確認執行狀態。

- **地圖中設置多個 `1`**
  程式僅辨識**第一個**掃描到的 `1` 作為起點，其餘 `1` 不具作用，視同一般座標處理。

- **對角線移動支援**
  不支援，`DIRECTIONS` 僅定義上下左右四個方向。

- **視覺上可行的地圖回報無解**
  規則要求路徑連續且每格僅經過一次；若地圖形狀導致搜尋過程中必然產生不可達格，即為無解，此為 `checkDead()` 檢測的目標情況。

---

# **OneLine Game Solver**

## **Overview**
Given a 2D grid map and a starting coordinate, traverse every walkable cell via a **single continuous path**, visiting each cell **exactly once**. This project solves the path using DFS with backtracking.

- **Map representation**: 2D list
  - `0`: walkable cell
  - `-1`: wall
  - `1`: start point (exactly one)
- **Search strategy**: DFS with backtracking; at each step, neighbors with the **fewest reachable cells** are expanded first (Warnsdorff's rule heuristic), reducing invalid branches
- **Pruning**: `checkDead()` checks after every step for unreachable cells (no walkable neighbors), terminating the branch early to avoid unnecessary search

## **Installation**
- **Runtime**: Python 3.x
- **Dependencies**: none, standard library only

```bash
git clone https://github.com/294Ryan/OneLine-Game-solver.git
```

## **Usage**
1. Edit the `_map` variable at the top of `OneLine_game_solver_v5_0.py` to define the target grid
2. Run:
   ```bash
   python OneLine_game_solver_v5_0.py
   ```
3. Output:
   - Map visualization: `▓` for wall, `▢` for walkable cell
   - If solvable: each cell's **visit order number** (1 = start)
   - If not solvable: `The map has no way to finish.`

## **FAQ**
- **Execution time is long**
  Worst-case complexity is exponential and scales sharply with map size. Progress is logged every 100,000 DFS calls (`DFS in N times.`) to confirm the process is still running.

- **Multiple `1` values in the map**
  Only the **first** `1` encountered during the scan is used as the start; any subsequent `1` values are treated as ordinary coordinates.

- **Diagonal movement**
  Not supported. `DIRECTIONS` only defines up, down, left, and right.

- **A visually solvable map reports no solution**
  The path must be continuous and visit each cell exactly once. If the map's shape forces an unreachable cell during search, it is genuinely unsolvable — this is the exact condition `checkDead()` detects.
