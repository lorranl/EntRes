from tkinter.filedialog import askopenfilename, asksaveasfilename

if __name__ == "__main__":

    basepath = askopenfilename(title="Select base file", filetypes=(("Text", "*.txt"), ("CSV", "*.csv")))
    comppath = askopenfilename(title="Select file to compare", filetypes=(("Text", "*.txt"), ("CSV", "*.csv")))
    tgtpath = asksaveasfilename(title="Select result as", defaultextension='.csv', filetypes=[("CSV", '*.csv')])

    


# TODO - Compare list within itself - identify possible duplicates
# TODO - Score based on token / regex matching
# TODO - Score based on levenshtein damerau calcs
