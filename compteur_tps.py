import tkinter as tk
from tkinter import ttk, font
from ttkthemes import ThemedTk
import tiktoken
import re
import difflib

# Dictionnaire de traductions mis à jour avec la nouvelle zone
TRANSLATIONS = {
    'fr': {'window_title': "Optimiseur de Tokens", 'model_label': "Type de modèle :", 'analyze_button': "Analyser / Surligner", 'optimize_button': "Optimiser le Texte ➔", 'truncate_button': "Tronquer l'Original", 'original_text_label': "Texte Original", 'optimized_text_label': "Texte Optimisé", 'tokens_label': "Tokens :", 'error_label': "Erreur", 'optimization_label': "Stratégie :", 'strategy_safe': "Légère (Code & Texte)", 'strategy_aggressive': "Agressive (Prose)", 'deleted_text_label': "Texte Supprimé :"},
    'en': {'window_title': "Token Optimizer", 'model_label': "Model type:", 'analyze_button': "Analyze / Highlight", 'optimize_button': "Optimize Text ➔", 'truncate_button': "Truncate Original", 'original_text_label': "Original Text", 'optimized_text_label': "Optimized Text", 'tokens_label': "Tokens:", 'error_label': "Error", 'optimization_label': "Strategy:", 'strategy_safe': "Safe (Code & Text)", 'strategy_aggressive': "Aggressive (Prose)", 'deleted_text_label': "Deleted Text:"},
    'es': {'window_title': "Optimizador de Tokens", 'model_label': "Tipo de modelo:", 'analyze_button': "Analizar / Resaltar", 'optimize_button': "Optimizar Texto ➔", 'truncate_button': "Truncar Original", 'original_text_label': "Texto Original", 'optimized_text_label': "Texto Optimizado", 'tokens_label': "Tokens:", 'error_label': "Error", 'optimization_label': "Estrategia:", 'strategy_safe': "Ligera (Código y Texto)", 'strategy_aggressive': "Agresiva (Prosa)", 'deleted_text_label': "Texto Eliminado:"},
    'it': {'window_title': "Ottimizzatore di Token", 'model_label': "Tipo di modello:", 'analyze_button': "Analizza / Evidenzia", 'optimize_button': "Ottimizza Testo ➔", 'truncate_button': "Tronca Originale", 'original_text_label': "Testo Originale", 'optimized_text_label': "Testo Ottimizzato", 'tokens_label': "Token:", 'error_label': "Errore", 'optimization_label': "Strategia:", 'strategy_safe': "Leggera (Codice e Testo)", 'strategy_aggressive': "Aggressiva (Prosa)", 'deleted_text_label': "Testo Eliminato:"},
    'pt': {'window_title': "Otimizador de Tokens", 'model_label': "Tipo de modelo:", 'analyze_button': "Analisar / Destacar", 'optimize_button': "Otimizar Texto ➔", 'truncate_button': "Truncar Original", 'original_text_label': "Texto Original", 'optimized_text_label': "Texto Otimizado", 'tokens_label': "Tokens:", 'error_label': "Erro", 'optimization_label': "Estratégia:", 'strategy_safe': "Leve (Código e Texto)", 'strategy_aggressive': "Agressiva (Prosa)", 'deleted_text_label': "Texto Excluído:"},
    'nl': {'window_title': "Token Optimalisator", 'model_label': "Modeltype:", 'analyze_button': "Analyseer / Markeer", 'optimize_button': "Optimaliseer Tekst ➔", 'truncate_button': "Origineel Afkappen", 'original_text_label': "Originele Tekst", 'optimized_text_label': "Geoptimaliseerde Tekst", 'tokens_label': "Tokens:", 'error_label': "Fout", 'optimization_label': "Strategie:", 'strategy_safe': "Veilig (Code & Tekst)", 'strategy_aggressive': "Agressief (Proza)", 'deleted_text_label': "Verwijderde Tekst:"},
    'pl': {'window_title': "Optymalizator Tokenów", 'model_label': "Typ modelu:", 'analyze_button': "Analizuj / Podświetl", 'optimize_button': "Optymalizuj Tekst ➔", 'truncate_button': "Utnij Oryginał", 'original_text_label': "Tekst Oryginalny", 'optimized_text_label': "Tekst Zoptymalizowany", 'tokens_label': "Tokeny:", 'error_label': "Błąd", 'optimization_label': "Strategia:", 'strategy_safe': "Bezpieczna (Kod i Tekst)", 'strategy_aggressive': "Agresywna (Proza)", 'deleted_text_label': "Usunięty Tekst:"},
    'hu': {'window_title': "Token Optimalizáló", 'model_label': "Modell típusa:", 'analyze_button': "Elemzés / Kiemelés", 'optimize_button': "Szöveg Optimalizálása ➔", 'truncate_button': "Eredeti Csonkítása", 'original_text_label': "Eredeti Szöveg", 'optimized_text_label': "Optimalizált Szöveg", 'tokens_label': "Tokenek:", 'error_label': "Hiba", 'optimization_label': "Stratégia:", 'strategy_safe': "Biztonságos (Kód és szöveg)", 'strategy_aggressive': "Agresszív (Próza)", 'deleted_text_label': "Törölt Szöveg:"},
    'el': {'window_title': "Βελτιστοποιητής Token", 'model_label': "Τύπος μοντέλου:", 'analyze_button': "Ανάλυση / Επισήμανση", 'optimize_button': "Βελτιστοποίηση Κειμένου ➔", 'truncate_button': "Περικοπή Πρωτότυπου", 'original_text_label': "Πρωτότυπο Κείμενο", 'optimized_text_label': "Βελτιστοποιημένο Κείμενο", 'tokens_label': "Token:", 'error_label': "Σφάλμα", 'optimization_label': "Στρατηγική:", 'strategy_safe': "Ασφαλής (Κώδικας & Κείμενο)", 'strategy_aggressive': "Επιθετική (Πεζογραφία)", 'deleted_text_label': "Κείμενο που διαγράφηκε:"},
    'ro': {'window_title': "Optimizator de Tokene", 'model_label': "Tip model:", 'analyze_button': "Analiză / Evidențiere", 'optimize_button': "Optimizare Text ➔", 'truncate_button': "Trunchere Original", 'original_text_label': "Text Original", 'optimized_text_label': "Text Optimizat", 'tokens_label': "Tokene:", 'error_label': "Eroare", 'optimization_label': "Strategie:", 'strategy_safe': "Sigură (Cod și Text)", 'strategy_aggressive': "Agresivă (Proză)", 'deleted_text_label': "Text Șters:"}
}
LANGUAGES = {'Français': 'fr', 'English': 'en', 'Español': 'es', 'Italiano': 'it', 'Português': 'pt', 'Nederlands': 'nl', 'Polski': 'pl', 'Magyar': 'hu', 'Ελληνικά': 'el', 'Română': 'ro'}
ENCODING_MAP = {"GPT-4, GPT-3.5 Turbo, Ada-002 (cl100k_base)": "cl100k_base", "Modèles Open-Source - Llama, Mistral (Approximation gpt2)": "gpt2", "Anciens modèles OpenAI - Davinci-003, Codex (p50k_base)": "p50k_base"}

def change_language(*args):
    lang_name = lang_combobox.get()
    lang_code = LANGUAGES.get(lang_name, 'fr')
    t = TRANSLATIONS[lang_code]
    window.title(t['window_title'])
    model_label.config(text=t['model_label'])
    analyze_button.config(text=t['analyze_button'])
    optimize_button.config(text=t['optimize_button'])
    truncate_button.config(text=t['truncate_button'])
    label_original.config(text=t['original_text_label'])
    label_optimized.config(text=t['optimized_text_label'])
    optimization_strategy_label.config(text=t['optimization_label'])
    optimization_strategy_combobox['values'] = (t['strategy_safe'], t['strategy_aggressive'])
    optimization_strategy_combobox.set(t['strategy_safe'])
    deleted_label.config(text=t['deleted_text_label'])
    result_label_original.config(text=f"{t['tokens_label']} 0")
    result_label_optimized.config(text=f"{t['tokens_label']} 0")

def _count_tokens_for_panel(text_widget, result_label, encoding):
    text_content = text_widget.get("1.0", "end-1c")
    lang_code = LANGUAGES.get(lang_combobox.get(), 'fr')
    t = TRANSLATIONS[lang_code]
    try:
        num_tokens = len(encoding.encode(text_content)) if text_content.strip() else 0
        result_label.config(text=f"{t['tokens_label']} {num_tokens}")
    except Exception:
        result_label.config(text=t['error_label'])

def analyze_and_highlight():
    text_input_original.tag_remove("highlight", "1.0", tk.END)
    text_input_optimized.tag_remove("highlight", "1.0", tk.END)
    deleted_text.delete("1.0", tk.END) # Nettoyer aussi la zone des suppressions
    encoding_name = ENCODING_MAP.get(encoding_combobox.get())
    if not encoding_name: return
    encoding = tiktoken.get_encoding(encoding_name)
    _highlight_panel(text_input_original, result_label_original, encoding)
    _highlight_panel(text_input_optimized, result_label_optimized, encoding)

def _highlight_panel(text_widget, result_label, encoding):
    _count_tokens_for_panel(text_widget, result_label, encoding)
    text_content = text_widget.get("1.0", "end-1c")
    if not text_content.strip(): return
    token_ids = encoding.encode(text_content)
    char_index = 0
    for i, token_id in enumerate(token_ids):
        token_text = encoding.decode([token_id])
        token_len = len(token_text)
        if i % 2 == 1:
            start_pos = f"1.0 + {char_index}c"
            end_pos = f"1.0 + {char_index + token_len}c"
            text_widget.tag_add("highlight", start_pos, end_pos)
        char_index += token_len

def optimize_text():
    # Nettoyer les anciens surlignages et la zone de suppression
    text_input_original.tag_remove("highlight", "1.0", tk.END)
    text_input_optimized.tag_remove("highlight", "1.0", tk.END)
    deleted_text.delete("1.0", tk.END)

    original_text = text_input_original.get("1.0", "end-1c")
    lang_code = LANGUAGES.get(lang_combobox.get(), 'fr')
    selected_strategy = optimization_strategy_combobox.get()
    
    if selected_strategy == TRANSLATIONS[lang_code]['strategy_safe']:
        lines = [line.rstrip() for line in original_text.splitlines()]
        optimized_text = "\n".join(lines)
        optimized_text = re.sub(r'\n{3,}', '\n\n', optimized_text)
    else:
        lines = (line.strip() for line in original_text.splitlines())
        optimized_text = "\n".join(lines)
        optimized_text = re.sub(r'\n{3,}', '\n\n', optimized_text)
        optimized_text = re.sub(r'[ \t]+', ' ', optimized_text)

    text_input_optimized.delete("1.0", tk.END)
    text_input_optimized.insert("1.0", optimized_text)
    
    # NOUVELLE LOGIQUE : Collecter les suppressions et les afficher
    deleted_parts = []
    matcher = difflib.SequenceMatcher(None, original_text, optimized_text, autojunk=False)
    for tag, i1, i2, j1, j2 in matcher.get_opcodes():
        if tag == 'delete' or tag == 'replace':
            # Remplacer les caractères non imprimables par leur représentation
            deleted_chunk = original_text[i1:i2].replace('\n', '\\n').replace('\t', '\\t')
            deleted_parts.append(deleted_chunk)
    
    if deleted_parts:
        deleted_text.insert("1.0", " | ".join(deleted_parts))

    encoding_name = ENCODING_MAP.get(encoding_combobox.get())
    if not encoding_name: return
    encoding = tiktoken.get_encoding(encoding_name)
    _count_tokens_for_panel(text_input_original, result_label_original, encoding)
    _count_tokens_for_panel(text_input_optimized, result_label_optimized, encoding)

def truncate_original_text():
    try: token_limit = int(token_limit_entry.get())
    except ValueError: return
    if token_limit <= 0: return
    encoding_name = ENCODING_MAP.get(encoding_combobox.get())
    if not encoding_name: return
    encoding = tiktoken.get_encoding(encoding_name)
    original_text = text_input_original.get("1.0", "end-1c")
    token_ids = encoding.encode(original_text)
    if len(token_ids) > token_limit:
        truncated_text = encoding.decode(token_ids[:token_limit])
        text_input_original.delete("1.0", tk.END)
        text_input_original.insert("1.0", truncated_text)
        analyze_and_highlight()

# --- Interface Graphique ---
window = ThemedTk(theme="arc")
window.geometry("1200x750") # Augmenter un peu la hauteur
main_frame = ttk.Frame(window, padding="10")
main_frame.pack(expand=True, fill=tk.BOTH)
config_frame = ttk.Frame(main_frame)
config_frame.pack(fill=tk.X, pady=(0, 10))
lang_combobox = ttk.Combobox(config_frame, values=list(LANGUAGES.keys()), state="readonly", width=12)
lang_combobox.pack(side=tk.LEFT, padx=(0, 20))
lang_combobox.set('Français')
lang_combobox.bind('<<ComboboxSelected>>', change_language)
model_label = ttk.Label(config_frame, text="")
model_label.pack(side=tk.LEFT, padx=(0, 10))
encoding_combobox = ttk.Combobox(config_frame, values=list(ENCODING_MAP.keys()), state="readonly")
encoding_combobox.current(0)
encoding_combobox.pack(side=tk.LEFT, fill=tk.X, expand=True)
actions_frame = ttk.Frame(main_frame)
actions_frame.pack(fill=tk.X, pady=5)
analyze_button = ttk.Button(actions_frame, command=analyze_and_highlight)
analyze_button.pack(side=tk.LEFT, expand=True, fill=tk.X, padx=5, ipady=4)
optimize_panel = ttk.Frame(actions_frame)
optimize_panel.pack(side=tk.LEFT, expand=True, fill=tk.X, padx=5)
optimization_strategy_label = ttk.Label(optimize_panel, text="")
optimization_strategy_label.pack(side=tk.LEFT, padx=(0, 5))
optimization_strategy_combobox = ttk.Combobox(optimize_panel, state="readonly", width=22)
optimization_strategy_combobox.pack(side=tk.LEFT, padx=(0, 10))
optimize_button = ttk.Button(optimize_panel, command=optimize_text)
optimize_button.pack(side=tk.LEFT, expand=True, fill=tk.X)
truncate_frame = ttk.Frame(actions_frame)
truncate_frame.pack(side=tk.LEFT, expand=True, fill=tk.X, padx=5)
token_limit_entry = ttk.Entry(truncate_frame, width=8)
token_limit_entry.insert(0, "4096")
token_limit_entry.pack(side=tk.LEFT)
truncate_button = ttk.Button(truncate_frame, command=truncate_original_text)
truncate_button.pack(side=tk.LEFT, fill=tk.X, expand=True)

# Cadre pour les deux panneaux principaux
text_panels_frame = ttk.Frame(main_frame)
text_panels_frame.pack(expand=True, fill=tk.BOTH, pady=(5,0))

def create_text_panel(parent):
    panel = ttk.Frame(parent, padding=5)
    safe_font = ("Segoe UI", 12, "bold")
    label = ttk.Label(panel, font=safe_font)
    label.pack(anchor="w")
    text_frame = ttk.Frame(panel)
    text_frame.pack(expand=True, fill=tk.BOTH)
    scrollbar = ttk.Scrollbar(text_frame)
    text_font = ("Segoe UI", 11)
    text_widget = tk.Text(text_frame, wrap="word", font=text_font, yscrollcommand=scrollbar.set, relief="solid", borderwidth=1)
    scrollbar.config(command=text_widget.yview)
    scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
    text_widget.pack(side=tk.LEFT, expand=True, fill=tk.BOTH)
    text_widget.tag_configure("highlight", background="#FFD700")
    result_label = ttk.Label(panel, font=(safe_font[0], 11, "bold"))
    result_label.pack(anchor="e", pady=(5,0))
    return panel, text_widget, result_label, label

left_panel, text_input_original, result_label_original, label_original = create_text_panel(text_panels_frame)
left_panel.pack(side=tk.LEFT, expand=True, fill=tk.BOTH, padx=(0, 5))
right_panel, text_input_optimized, result_label_optimized, label_optimized = create_text_panel(text_panels_frame)
right_panel.pack(side=tk.LEFT, expand=True, fill=tk.BOTH, padx=(5, 0))

# NOUVEAU : Cadre pour le texte supprimé en bas
deleted_frame = ttk.Frame(main_frame, padding=5)
deleted_frame.pack(fill=tk.X, pady=(5,0))
deleted_label = ttk.Label(deleted_frame, font=("Segoe UI", 12, "bold"))
deleted_label.pack(anchor="w")
deleted_text_frame = ttk.Frame(deleted_frame)
deleted_text_frame.pack(expand=True, fill=tk.BOTH, pady=(5,0))
deleted_yscroll = ttk.Scrollbar(deleted_text_frame, orient='vertical')
deleted_xscroll = ttk.Scrollbar(deleted_text_frame, orient='horizontal')
deleted_text = tk.Text(
    deleted_text_frame, height=3, relief="solid", borderwidth=1,
    wrap="none", # Important pour le défilement horizontal
    yscrollcommand=deleted_yscroll.set,
    xscrollcommand=deleted_xscroll.set,
    font=("Segoe UI", 10), foreground="gray"
)
deleted_yscroll.config(command=deleted_text.yview)
deleted_xscroll.config(command=deleted_text.xview)
deleted_yscroll.pack(side=tk.RIGHT, fill=tk.Y)
deleted_xscroll.pack(side=tk.BOTTOM, fill=tk.X)
deleted_text.pack(expand=True, fill=tk.BOTH)

change_language()
window.mainloop()