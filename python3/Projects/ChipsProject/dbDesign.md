Chips

    chip_id             (unique identifier for each chip)
    chip_name           (name of the chip)
    manufacturer        (name of the company that makes the chip)
    year_of_manufacture (year in which the chip was manufactured)
    transistor_count    (number of transistors in the chip)

Transistors

    transistor_id   (unique identifier for each transistor)
    chip_id         (the chip that the transistor belongs to, as a foreign key referencing Chips.chip_id)
    gate_type       (the type of gate used in the transistor)
    material        (the material used to make the transistor)
    size            (the size of the transistor)

Revenue

    revenue_id  (unique identifier for each revenue entry)
    chip_id     (the chip that generated the revenue, as a foreign key referencing Chips.chip_id)
    date        (the date when the revenue was generated)
    amount      (the amount of revenue generated)
