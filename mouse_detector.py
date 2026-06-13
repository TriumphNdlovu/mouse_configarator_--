import hid

def detect_logitech_devices():
    devices = hid.enumerate()

    found_devices = []

    for device in devices:
        manufacturer = device.get("manufacturer_string")
        product = device.get("product_string")

        if manufacturer and "Logitech" in manufacturer:
            found_devices.append({
                "product": product,
                "vendor_id": device["vendor_id"],
                "product_id": device["product_id"]
            })

    return found_devices