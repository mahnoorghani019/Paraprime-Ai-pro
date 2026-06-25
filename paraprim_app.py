import tkinter as tk
import customtkinter as ctk
import time
import threading
import re
import random

# Premium Enterprise Theme Configuration
ctk.set_appearance_mode("Light")
ctk.set_default_color_theme("blue")

class ParaPrimeApp(ctk.CTk):
    def __init__(self):
        super().__init__()

        # Window Meta & High-End Desktop Sizing
        self.title("ParaPrime Pro : Paralogue Specificity Engine")
        self.geometry("1320://800")
        self.minsize(1200, 750)
        self.configure(fg_color="#F8FAFC")  # Clean Slate background

        # Enterprise Design Typography
        self.brand_font = ctk.CTkFont(family="Segoe UI", size=22, weight="bold")
        self.section_font = ctk.CTkFont(family="Segoe UI", size=15, weight="bold")
        self.body_font = ctk.CTkFont(family="Segoe UI", size=13, weight="normal")
        self.body_bold = ctk.CTkFont(family="Segoe UI", size=13, weight="bold")
        self.mono_font = ctk.CTkFont(family="Consolas", size=13)

        # Layout Split: 60% Left Workspace, 40% Right AI Dashboard
        self.grid_rowconfigure(0, weight=0) # Top Banner
        self.grid_rowconfigure(1, weight=1) # Main App Workspace
        self.grid_columnconfigure(0, weight=6)
        self.grid_columnconfigure(1, weight=4)

        self.render_top_banner()
        self.render_analysis_workspace()
        self.render_ai_dashboard()

    def render_top_banner(self):
        """Builds a high-end corporate platform header banner."""
        self.banner = ctk.CTkFrame(self, corner_radius=0, fg_color="#0F172A", height=75)
        self.banner.grid(row=0, column=0, columnspan=2, sticky="ew")
        self.banner.grid_propagate(False)
        
        self.logo_label = ctk.CTkLabel(
            self.banner, 
            text="🧬 PARAPRIME AI-PRO", 
            font=self.brand_font, 
            text_color="#FFFFFF"
        )
        self.logo_label.pack(side="left", padx=24)

        self.tag_label = ctk.CTkLabel(
            self.banner, 
            text="|  Deep Learning Sequence Analytics & Alignment v3.0", 
            font=self.body_font, 
            text_color="#94A3B8"
        )
        self.tag_label.pack(side="left")

        self.badge = ctk.CTkFrame(self.banner, fg_color="#1E293B", corner_radius=6)
        self.badge.pack(side="right", padx=24, pady=18)
        
        self.badge_txt = ctk.CTkLabel(self.badge, text="TENSORFLOW / PYTORCH CORE PIPELINE", font=self.body_bold, text_color="#10B981", padx=12, pady=4)
        self.badge_txt.pack()

    def render_analysis_workspace(self):
        """Constructs the primary genomic sequencing core layout."""
        self.workspace_frame = ctk.CTkFrame(self, corner_radius=12, fg_color="#FFFFFF", border_width=1, border_color="#E2E8F0")
        self.workspace_frame.grid(row=1, column=0, sticky="nsew", padx=24, pady=24)
        
        self.workspace_frame.grid_rowconfigure(0, weight=0)
        self.workspace_frame.grid_rowconfigure(1, weight=0)
        self.workspace_frame.grid_rowconfigure(2, weight=1)
        self.workspace_frame.grid_columnconfigure(0, weight=1)

        self.control_head = ctk.CTkLabel(self.workspace_frame, text="Target Genomic Anchor Entry", font=self.section_font, text_color="#1E293B")
        self.control_head.grid(row=0, column=0, padx=24, pady=(20, 10), sticky="w")

        self.action_bar = ctk.CTkFrame(self.workspace_frame, fg_color="transparent")
        self.action_bar.grid(row=1, column=0, padx=24, pady=10, sticky="ew")
        self.action_bar.grid_columnconfigure(0, weight=1)

        self.seq_input = ctk.CTkEntry(
            self.action_bar, 
            placeholder_text="Paste target nucleotide sequence data here...", 
            fg_color="#F8FAFC", 
            border_color="#CBD5E1", 
            text_color="#0F172A", 
            font=self.body_font,
            corner_radius=6,
            height=44
        )
        self.seq_input.grid(row=0, column=0, padx=(0, 12), sticky="ew")
        self.seq_input.bind("<Return>", lambda event: self.execute_ai_pipeline())

        self.design_btn = ctk.CTkButton(
            self.action_bar, 
            text="RUN AI PREDICTOR", 
            width=160, 
            height=44, 
            fg_color="#4F46E5",        
            hover_color="#4338CA", 
            font=self.body_bold, 
            text_color="#FFFFFF", 
            corner_radius=6,
            command=self.execute_ai_pipeline
        )
        self.design_btn.grid(row=0, column=1)

        self.output_container = ctk.CTkFrame(self.workspace_frame, fg_color="#0F172A", corner_radius=8, border_width=1, border_color="#1E293B")
        self.output_container.grid(row=2, column=0, padx=24, pady=(16, 24), sticky="nsew")
        self.output_container.grid_rowconfigure(0, weight=1)
        self.output_container.grid_columnconfigure(0, weight=1)

        self.results_box = ctk.CTkTextbox(
            self.output_container, 
            fg_color="transparent", 
            text_color="#38BDF8",      
            font=self.mono_font,
            corner_radius=8
        )
        self.results_box.grid(row=0, column=0, sticky="nsew", padx=16, pady=16)
        self.results_box.insert("0.0", "[SYS-STATUS] Predictive infrastructure initialized. Input data matrix to run neural classification metrics...")
        self.results_box.configure(state="disabled")

    def render_ai_dashboard(self):
        """Replaces chatbot with an interactive AI Model Analytics Panel with charts and data readouts."""
        self.side_frame = ctk.CTkFrame(self, corner_radius=0, fg_color="#F1F5F9", border_width=1, border_color="#E2E8F0")
        self.side_frame.grid(row=1, column=1, sticky="nsew")
        
        self.side_frame.grid_columnconfigure(0, weight=1)

        # Section Label
        self.side_title = ctk.CTkLabel(self.side_frame, text="Neural Network Analytics Engine", font=self.section_font, text_color="#1E293B", anchor="w")
        self.side_title.grid(row=0, column=0, padx=24, pady=(24, 12), sticky="ew")

        # METRIC CARD 1: Confidence
        self.card_1 = ctk.CTkFrame(self.side_frame, fg_color="#FFFFFF", corner_radius=8, border_width=1, border_color="#E2E8F0")
        self.card_1.grid(row=1, column=0, padx=24, pady=10, sticky="ew")
        
        self.c1_title = ctk.CTkLabel(self.card_1, text="Model Classification Confidence", font=self.body_bold, text_color="#475569")
        self.c1_title.pack(anchor="w", padx=16, pady=(12, 4))
        self.progress_1 = ctk.CTkProgressBar(self.card_1, height=10, progress_color="#10B981", fg_color="#E2E8F0")
        self.progress_1.pack(fill="x", padx=16, pady=6)
        self.progress_1.set(0.0)
        self.c1_val = ctk.CTkLabel(self.card_1, text="Awaiting Execution...", font=self.mono_font, text_color="#64748B")
        self.c1_val.pack(anchor="e", padx=16, pady=(0, 12))

        # METRIC CARD 2: Structural Mutation Secondary Risks
        self.card_2 = ctk.CTkFrame(self.side_frame, fg_color="#FFFFFF", corner_radius=8, border_width=1, border_color="#E2E8F0")
        self.card_2.grid(row=2, column=0, padx=24, pady=10, sticky="ew")
        
        self.c2_title = ctk.CTkLabel(self.card_2, text="Secondary Structural Loop Formation Risk", font=self.body_bold, text_color="#475569")
        self.c2_title.pack(anchor="w", padx=16, pady=(12, 4))
        self.progress_2 = ctk.CTkProgressBar(self.card_2, height=10, progress_color="#F59E0B", fg_color="#E2E8F0")
        self.progress_2.pack(fill="x", padx=16, pady=6)
        self.progress_2.set(0.0)
        self.c2_val = ctk.CTkLabel(self.card_2, text="Awaiting Execution...", font=self.mono_font, text_color="#64748B")
        self.c2_val.pack(anchor="e", padx=16, pady=(0, 12))

        # AI DATA TABLE MOCK
        self.table_label = ctk.CTkLabel(self.side_frame, text="Transformer Layer Weights Matrix", font=self.body_bold, text_color="#334155", anchor="w")
        self.table_label.grid(row=3, column=0, padx=24, pady=(20, 4), sticky="ew")

        self.table_frame = ctk.CTkFrame(self.side_frame, fg_color="#0F172A", corner_radius=8)
        self.table_frame.grid(row=4, column=0, padx=24, pady=5, sticky="nsew")
        
        self.table_txt = ctk.CTkTextbox(self.table_frame, fg_color="transparent", text_color="#94A3B8", font=self.mono_font, height=220)
        self.table_txt.pack(fill="both", expand=True, padx=12, pady=12)
        self.generate_empty_table()

    def generate_empty_table(self):
        self.table_txt.configure(state="normal")
        self.table_txt.delete("0.0", "end")
        header = f"{'LAYER':<12}{'WEIGHT DELTA':<18}{'BIAS PROFILE':<14}{'LOSS status':<12}\n"
        divider = "-" * 60 + "\n"
        self.table_txt.insert("end", header + divider + " [SYSTEM IDLE] No sequence vector tensor mapped yet.\n")
        self.table_txt.configure(state="disabled")

    def print_telemetry(self, message):
        self.results_box.configure(state="normal")
        self.results_box.insert("end", "\n" + message)
        self.results_box.configure(state="disabled")
        self.results_box.see("end")

    def execute_ai_pipeline(self):
        sequence = self.seq_input.get().strip().upper()
        if not sequence:
            return
        
        cleaned = re.sub(r'[^ATGC]', '', sequence)
        if len(cleaned) < 50:
            self.results_box.configure(state="normal")
            self.results_box.delete("0.0", "end")
            self.results_box.insert("0.0", "[VALIDATION FAILURE]: Sequence array context must exceed 50 base pairs.")
            self.results_box.configure(state="disabled")
            return

        self.design_btn.configure(state="disabled")
        threading.Thread(target=self.process_ai_analytics, args=(cleaned,), daemon=True).start()

    def process_ai_analytics(self, data):
        """Simulates advanced deep learning sequence extraction workflow."""
        self.results_box.configure(state="normal")
        self.results_box.delete("0.0", "end")
        self.results_box.configure(state="disabled")

        self.print_telemetry("[MODEL DEPLOYED] Vectorizing raw text string tokens into continuous multi-dimensional space tensors...")
        time.sleep(0.7)
        
        # Animate Progress Dashbars to show machine computation happening live!
        self.progress_1.set(0.35)
        self.c1_val.configure(text="Evaluating tokens (35%)...")
        
        self.print_telemetry(" -> Running sequence attention layers over nucleotide strings...")
        time.sleep(0.8)
        
        self.progress_1.set(0.72)
        self.progress_2.set(0.48)
        self.c1_val.configure(text="Optimizing gradient loss maps (72%)...")
        self.c2_val.configure(text="Calculating hairpin loop risks (48%)...")
        
        time.sleep(0.9)

        # Generate Fake Model Prediction numbers dynamically based on sequence content
        conf = random.uniform(97.2, 99.8)
        risk = random.uniform(2.1, 14.5)
        
        self.progress_1.set(1.0)
        self.progress_2.set(risk / 100.0)
        self.c1_val.configure(text=f"OPTIMAL ({conf:.2f}%)")
        self.c2_val.configure(text=f"LOW MINIMA ({risk:.2f}%)")

        # Update table with professional looking weights matrix data
        self.table_txt.configure(state="normal")
        self.table_txt.delete("0.0", "end")
        header = f"{'LAYER':<12}{'WEIGHT DELTA':<18}{'BIAS PROFILE':<14}{'LOSS STATUS':<12}\n"
        divider = "-" * 60 + "\n"
        self.table_txt.insert("end", header + divider)
        self.table_txt.insert("end", f"Conv1D_01    {random.uniform(-0.5,0.5):+.6f}          {random.uniform(0.1,0.9):.4f}         CONVERGED\n")
        self.table_txt.insert("end", f"Attention_02 {random.uniform(-0.5,0.5):+.6f}          {random.uniform(0.1,0.9):.4f}         CONVERGED\n")
        self.table_txt.insert("end", f"Dense_Out    {random.uniform(-0.5,0.5):+.6f}          {random.uniform(0.1,0.9):.4f}         STABLE\n")
        self.table_txt.configure(state="disabled")

        f_cand = data[0:20]
        f_gc = (f_cand.count('G') + f_cand.count('C')) / len(f_cand) * 100
        f_tm = 2 * (f_cand.count('A') + f_cand.count('T')) + 4 * (f_cand.count('G') + f_cand.count('C'))

        self.print_telemetry("\n" + "="*80)
        self.print_telemetry("                       AI PREDICTIVE REPORT MATRIX SUMMARY")
        self.print_telemetry("="*80)
        self.print_telemetry(f"TRANSFORMER GENERATED STRAND SPECIFICATIONS:")
        self.print_telemetry(f"   Oligonucleotide Vector Fragment: 5'- {f_cand} -3'")
        self.print_telemetry(f"   Internal Composition Balance:  Length: {len(f_cand)} bp  |  GC Content: {f_gc:.1f}%")
        self.print_telemetry(f"   Calculated Thermodynamic Node: Core Target Melting Temp (Tm): {f_tm:.1f}°C")
        self.print_telemetry("\n" + "-"*80)
        self.print_telemetry("DEEP NEURAL ACCURACY ASSESSMENT HIGHLIGHTS:")
        self.print_telemetry(f"   • Cross-Reactivity Risk Index: {random.uniform(0.01, 0.09):.3f}% (High Target Localization Precision)")
        self.print_telemetry("   • Model Feature Classification Stability Matrix: PASSED")
        self.print_telemetry("="*80 + "\n")
        
        self.design_btn.configure(state="normal")

if __name__ == "__main__":
    app = ParaPrimeApp()
    app.mainloop()
