# Sivasankar's keyboard
One day, I was thinking about making a custom keyboard which would be suitable for me from scratch but that was too costly. After i joined hackclub's stasis i thought why not to build our keyboard as the stasis event funds us. So i started making a custom 75 percent keyboard from scratch using fusion 360 and kicad. I used the layout keycool 84 which had 84 keys in it.
# Layout
![](https://github.com/sasukeop108/Sivasankar-s-Keyboard/blob/main/Assets/keyboard-layout%20(1).png)
# CAD
![](https://github.com/sasukeop108/Sivasankar-s-Keyboard/blob/main/Assets/assembly.png)
![](https://github.com/sasukeop108/Sivasankar-s-Keyboard/blob/main/Assets/keebcase.png)
![](https://github.com/sasukeop108/Sivasankar-s-Keyboard/blob/main/Assets/keebcasedown.png)
# PCB
![](https://github.com/sasukeop108/Sivasankar-s-Keyboard/blob/main/Assets/pcbroute.png)
![](https://github.com/sasukeop108/Sivasankar-s-Keyboard/blob/main/Assets/pcb_3d.png)
# SCHEMATIC
![](https://github.com/sasukeop108/Sivasankar-s-Keyboard/blob/main/Assets/keebsch.png)
# BOM
| Name | Purpose | Cost Per Item (USD) | Quantity | Total (USD) | Link | Distributor |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 3d case | for housing keyboard | 8.50 | 1 | 8.50 | | printing legion |
| switches | for input to raspberry pi pico | 2.14 | 9 | 19.26 | [Cosmic Byte](https://www.thecosmicbyte.com/product/gateron-mechanical-switches-compatible-with-cosmic-byte-hot-swappable-keyboards-qty-1pc/) | cosmic byte |
| raspberry pi pico | for controlling everything | 0.00 | 1 | 0.00 | | self sourced |
| custom pcb | for soldering all components on | 40.65 | 1 | 40.65 | | jlcpcb |
| stabilizers | for bigger keycaps | 17.05 | 1 | 17.05 | [StacksKB](https://stackskb.com) | stackskb |
| keycaps | keys for typing | 13.89 | 1 | 13.89 | [StacksKB](https://stackskb.com/store/veekos-gradient-keycaps-cherry-profile-135-keys/) | stackskb |
| **Grand Total** | | | | **99.35** | | |
# Flashing instructions
download the keyboard.py from, the firmware folder and import it into circuit python select the com ports and youre ready to flash the code.
