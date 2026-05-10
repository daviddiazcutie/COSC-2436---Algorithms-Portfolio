class Box:
    def __init__(self, label: str, length: float, width: float, height: float):
        self.label = label
        self.length = length
        self.width = width
        self.height = height

    def volume(self) -> float:
        """Calculate the volume of the box."""
        return self.length * self.width * self.height


def pack_truck(boxes: list, truck_volume: float) -> list:
    """Pack the truck using a greedy strategy based on box volumes."""
    sorted_boxes = sorted(boxes, key=lambda b: b.volume(), reverse=True)

    packed_boxes = []
    used_volume = 0.0

    for box in sorted_boxes:
        box_vol = box.volume()
        if used_volume + box_vol <= truck_volume:
            packed_boxes.append(box)
            used_volume += box_vol

    return packed_boxes


if __name__ == "__main__":
    print("Welcome to the Truck Cargo Calculator")
    print("This program helps you calculate how to pack your cargo efficiently using a greedy algorithm.\n")

    # Truck dimensions
    print("Enter truck dimensions:")
    truck_length = float(input("  Length: "))
    truck_width  = float(input("  Width:  "))
    truck_height = float(input("  Height: "))
    truck_volume = truck_length * truck_width * truck_height
    print(f"Truck volume: {truck_volume:.2f} cubic units\n")

    # Input boxes
    boxes = []
    print("Enter box details (type 'done' as the label to finish):")
    while True:
        label = input("\n  Box label: ").strip()
        if label.lower() == "done":
            break
        length = float(input("  Length: "))
        width  = float(input("  Width:  "))
        height = float(input("  Height: "))
        boxes.append(Box(label, length, width, height))

    # Pack and display results
    packed = pack_truck(boxes, truck_volume)
    total_used = sum(b.volume() for b in packed)

    print("\n--- Packing Results ---")
    if packed:
        print(f"Packed {len(packed)} of {len(boxes)} box(es):")
        for b in packed:
            print(f"  • {b.label}: {b.volume():.2f} cubic units")
        print(f"\nVolume used : {total_used:.2f} / {truck_volume:.2f} cubic units")
        print(f"Utilization : {(total_used / truck_volume) * 100:.1f}%")
    else:
        print("No boxes could fit in the truck.")

    print("\nThank you for using the Truck Cargo Calculator.")
