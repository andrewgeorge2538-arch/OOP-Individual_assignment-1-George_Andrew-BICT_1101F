# Crop Yield Monitoring System

A simple Python program that helps record and compare crop harvests on small farms in Sierra Leone.
Built for PROG211 Object-Oriented Programming 1 (Limkokwing University of Creative Technology, Sierra Leone).

## The problem
Many small farmers do not keep records of how much they plant and harvest. Without records it is hard to see which
crops do well, plan the next season, or report to agricultural officers. This program gives a simple, free way to
store harvest records and calculate yield (kilograms per hectare).

## How to run
Requires Python 3.8 or newer. No extra packages are needed.

```
python main.py
```

## Example usage

```
=== Crop Yield Monitoring System ===

1. Add farm
2. Add harvest record
3. View all farms
4. Exit
Choose an option: 1
Enter farm as ID,District,Chiefdom (e.g. F001,Bo,Tikonko): F001,Bo,Tikonko
Farm F001 added.

Choose an option: 2
Farm ID: f001
Crop (rice, cassava, groundnut, cocoa, maize): rice
Season (e.g. 2026-Rainy): 2026-Rainy
Area planted (hectares): 2
Harvest (kg): 3000
Record saved. Yield: 1500.0 kg/ha

Choose an option: 3
Farm F001 - Bo, Tikonko
  Records: 1 | Average yield: 1500.0 kg/ha
  Latest record:
  2026-Rainy | Rice | 2 ha | 3000 kg | 1500.0 kg/ha
```

## Files
| File | Purpose |
|------|---------|
| `models.py` | The classes `CropRecord` and `Farm` |
| `main.py` | Menu, input checks, and the dictionary that stores farms |
| `LICENSE` | MIT open-source licence |

## OOP concepts used
- **Classes and objects:** `Farm` and `CropRecord`, each with attributes and methods. A `Farm` object receives `CropRecord` objects through `add_record()`.
- **Data structure:** one dictionary, `farms`, stores `Farm` objects using the farm ID as the key. The functions `add_farm()` and `display_farms()` add and show records.
- **Instance methods:** `yield_per_ha()`, `display_info()`, `add_record()`, `average_yield()`.
- **Class method:** `CropRecord.get_record_count()` and `Farm.from_text()` (`@classmethod`).
- **Static method:** `CropRecord.is_valid_crop()` (`@staticmethod`).
- **Tuples:** `SUPPORTED_CROPS` and each farm's `location` (district, chiefdom) are tuples because they should not change.

## Digital Public Goods (DPG) alignment
| Principle | How this project meets it |
|-----------|---------------------------|
| Open source | Published on GitHub under the MIT licence, so anyone can use, study, and improve it. |
| Inclusive and accessible | Plain text menu with short instructions; works offline on low-cost computers; no internet, account, or paid software needed; clear error messages for wrong input. |
| Privacy-respecting | No names, phone numbers, or other personal data are stored. Farms use an anonymous ID and only a district and chiefdom. Data stays in memory and is not sent anywhere. |
| Modular and reusable | Classes are in `models.py`, separate from the menu in `main.py`, so another program (for example a mobile or web app) can reuse them. Crop types are kept in one tuple and are easy to change. |

## Limitations
Data is kept in memory only and is lost when the program closes. Saving to a file or database could be added later.

## Licence
MIT. See the `LICENSE` file.
