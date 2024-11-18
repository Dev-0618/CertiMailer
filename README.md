# CertiMailer

### Instructions to Set Up CertiMailer  

1. **Clone the Repository**  
   ```bash
   git clone https://github.com/Dev-0618/CertiMailer
   cd CertiMailer
   ```

2. **Install Dependencies**  
   ```bash
   pip install -r requirements.txt
   ```

3. **Update File Paths and Values**  
   - **`cert.py`:**  
     - Set the template path: `template/certificate.png`.  
     - Update font: `font/cert_font.ttf`.  
     - Adjust text placement (`text_x`, `text_y`): Use an editor to find the correct coordinates.  
     - Ensure `output/` folder exists for generated certificates.  

   - **`send-email.py`:**  
     - Ensure `participants.csv` has **Name** and **Email** columns.  
     - Verify `output/{name}_certificate.png` for correct certificate paths.  
     - Credentials (email & app password) will save to `cred.txt` after first run.  

4. **Run Certificate Generator**  
   ```bash
   python cert.py
   ```

5. **Send Emails**  
   ```bash
   python send-email.py
   ```

---

**Note:** Customize paths, font, and placement values in the scripts as needed. Refer to your template for alignment and folder structure.
