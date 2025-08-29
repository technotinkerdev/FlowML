# FlowML
An mark-up language that converts JavaScript Object Notation data into easy to understand flow chart. Its at the alpha stage right now, We are looking forward to make this better. Contributors: Techno Tinker, Creaminit1234
Thanks for sharing the image and input data! Here's a clear explanation of your project:

---

### 🛠️ **Flow ml (Alpha Stage)**

**Flow ml** is a markup language currently in its **alpha stage**, designed to convert **JSON (JavaScript Object Notation)** data into easy-to-understand **flowcharts**. The goal is to make it simple to represent logical processes visually by just providing structured input.

---

### 📥 Input (JSON):

```json
{
  "start": "Start Process",
  "steps": {
    "Start Process": {
      "next": "Check Condition"
    },
    "Check Condition": {
      "yes": "Step A",
      "no": "Step B"
    },
    "Step A": {
      "next": "End"
    },
    "Step B": {
      "next": "End"
    }
  },
  "end": "End"
}
```

---

### 🖼️ Output (Flowchart):

<img width="227" height="371" alt="flowchart" src="https://github.com/user-attachments/assets/f1ac5c81-db0d-45f4-b6f5-c861a0e34402" />

---

### 👨‍💻 Contributors:

* **Techno Tinker**
* **Creaminit1234**

---

### 🚧 Note:

FlowML is **currently in alpha**. The team is actively working on improving it, and your feedback will help make it better. Stay tuned for updates!

Would you like help creating a README or web documentation for this?
