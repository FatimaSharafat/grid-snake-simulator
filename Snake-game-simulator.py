"""
Grid Snake Simulator
=====================
A random-walk simulation of a "snake" crossing an N x N grid from the
top-left corner. At each step the snake moves right or down with equal
probability (down is forced once it reaches the last column). Every move
costs energy; landing on a cell where (row + col) % bonus_modulus == 0
refunds energy. The run ends when the snake reaches the last row or
runs out of energy, and the full path it traced is rendered as a grid.
"""
from __future__ import annotations
import random
from dataclasses import dataclass
from typing import List, Optional, Tuple
Cell = Tuple[int, int]
@dataclass(frozen=True)
class SimulationConfig:
 grid_size: int = 50
 starting_energy: int = 50
 energy_per_move: int = 1
 bonus_energy: int = 5
 bonus_modulus: int = 10
@dataclass
class SimulationResult:
 path: List[Cell]
 moves: int
 remaining_energy: int
 final_position: Cell
 reason: str
def simulate(config: SimulationConfig = SimulationConfig(), seed: Optional[int] = None) -> SimulationResult:
 """Run the random-walk simulation and return the full path taken."""
 if seed is not None:
 random.seed(seed)
 last_index = config.grid_size - 1
 row, col = 0, 0
 energy = config.starting_energy
 moves = 0
 path: List[Cell] = [(row, col)]
 while row < last_index and energy > 0:
 can_move_right = col < last_index
 if can_move_right and random.random() < 0.5:
 col += 1
 else:
 row += 1
 moves += 1
 energy -= config.energy_per_move
 if (row + col) % config.bonus_modulus == 0:
 energy += config.bonus_energy
 path.append((row, col))
 reason = "Reached the bottom" if row >= last_index else "Out of energy"
 return SimulationResult(
 path=path,
 moves=moves,
 remaining_energy=energy,
 final_position=(row, col),
  )
def render(result: SimulationResult, config: SimulationConfig, use_color: bool = True) -> str:
 """Render every row the snake reached, marking visited cells as 'O' and the rest as 'X'."""
 visited = set(result.path)
 last_row_reached = result.final_position[0]
 red, reset = ("\033[31m", "\033[0m") if use_color else ("", "")
 lines = []
 for r in range(last_row_reached + 1):
 row_chars = [f"{red}O{reset}" if (r, c) in visited else "X" for c in range(config.grid_size)]
 lines.append(" ".join(row_chars))
 return "\n".join(lines)
def main() -> None:
 config = SimulationConfig()
 result = simulate(config)
 print(render(result, config))
 print("\nGame Over!\n")
 print(f"Reason: {result.reason}")
 print(f"Total Moves: {result.moves}")
 print(f"Remaining Energy: {result.remaining_energy}")
 print(f"Final Position: {result.final_position}")
if __name__ == "__main__":
 main()
