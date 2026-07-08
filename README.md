■[中文](#一筆畫遊戲解法器)    ■[English](#oneline-game-solver)

# **一筆畫遊戲解法器**

## **這是什麼**
給定一張地圖（2D 網格）與一個起點，用**一條連續路徑**走完所有可走格子，且**每格只能經過一次**。本專案用 DFS + 回溯自動找出這條路徑。

- **地圖表示**：二維 list
  - `0` = 可走格
  - `-1` = 牆
  - `1` = 起點（只能有一個）
- **核心演算法**：DFS 回溯，每步優先嘗試「周圍可走格數最少」的方向（類似 Warnsdorff's rule），減少無效搜尋
- **剪枝機制**：`checkDead()` 會即時偵測地圖上是否出現「孤島格」（被困死、無法再被走到的格子），一旦出現就提前放棄該分支

## **安裝**
- **需求**：Python 3.x
- **相依套件**：無，純標準庫

```bash
git clone https://github.com/294Ryan/OneLine-Game-solver.git
```

## **快速上手**
1. 打開 `OneLine_game_solver_v5_0.py`，直接修改檔案開頭的 `_map` 變數成你要的地圖
2. 執行：
   ```bash
   python OneLine_game_solver_v5_0.py
   ```
3. 輸出內容：
   - 先印出地圖示意圖：`▓` = 牆、`▢` = 路
   - 有解：印出每格的**走訪順序編號**（1 為起點）
   - 無解：印出 `The map has no way to finish.`

## **常見問題**
- **跑很久沒反應？**
  大地圖在最差情況下是指數複雜度。程式每執行 10 萬次 DFS 會印一次進度（`DFS in N times.`），確認是仍在跑而非卡死。

- **地圖裡可以有多個起點（`1`）嗎？**
  不行，程式只認**第一個**找到的 `1`，其餘 `1` 不會被特別處理。

- **支援斜向移動嗎？**
  不支援，`DIRECTIONS` 只定義上下左右四個方向。

- **為什麼有些明明看起來能走完的地圖卻回報無解？**
  規則是「每格只能經過一次、且路徑必須連續」，如果地圖形狀導致中途必然產生孤立格（無法再被任何方向走到），就無解——這正是 `checkDead()` 檢查的情況。

---

# **OneLine Game Solver**

## **What It Does**
Given a grid map and a starting point, find **one continuous path** that visits every walkable cell **exactly once**. This project solves it with DFS + backtracking.

- **Map format**: 2D list
  - `0` = walkable cell
  - `-1` = wall
  - `1` = start point (only one allowed)
- **Core algorithm**: DFS with backtracking, prioritizing the neighbor with the **fewest available moves** at each step (similar to Warnsdorff's rule) to cut down search space
- **Pruning**: `checkDead()` detects "dead" cells in real time — cells that become unreachable — and abandons that branch early

## **Install**
- **Requirement**: Python 3.x
- **Dependencies**: none, standard library only

```bash
git clone https://github.com/294Ryan/OneLine-Game-solver.git
```

## **Quick Start**
1. Open `OneLine_game_solver_v5_0.py` and edit the `_map` variable at the top of the file to your target grid
2. Run:
   ```bash
   python OneLine_game_solver_v5_0.py
   ```
3. Output:
   - Prints the map first: `▓` = wall, `▢` = road
   - If solvable: prints each cell's **visit order number** (1 = start)
   - If not solvable: prints `The map has no way to finish.`

## **FAQ**
- **It's taking forever — is it stuck?**
  Worst-case complexity is exponential for large maps. The script prints progress every 100,000 DFS calls (`DFS in N times.`) so you can confirm it's still running.

- **Can I have more than one `1` in the map?**
  No, only the **first** `1` found is used as the start; any others are ignored.

- **Does it support diagonal moves?**
  No, `DIRECTIONS` only defines up/down/left/right.

- **Why does a map that looks solvable still return no solution?**
  The rule requires every cell visited exactly once via a continuous path. If the shape forces an unreachable cell mid-solve, it's genuinely unsolvable — that's exactly what `checkDead()` catches.
