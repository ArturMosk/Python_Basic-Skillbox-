def form_histograma(text):
    histogramma = dict()
    for symbol in text:
        if symbol in histogramma:
            histogramma[symbol] += 1
        else:
            histogramma[symbol] = 1

    return histogramma


def form_histogramma_inverted(histogramma):
    histogramma_inverted = dict()
    frequency = set(histogramma.values())
    for element in frequency:
        letters = []
        for letter, freq in histogramma.items():
            if freq == element:
                letters.append(letter)
        histogramma_inverted[element] = letters

    return histogramma_inverted


user_text = input('Введите текст: ').lower()

hist = form_histograma(user_text)
print('Оригинальный словарь частот:')
for letter in sorted(hist.keys()):
    print(letter, ':', hist[letter])

hist_inv = form_histogramma_inverted(hist)
print('\nИнвертированный словарь частот:')
for freq in sorted(hist_inv.keys()):
    print(freq, ':', hist_inv[freq])
