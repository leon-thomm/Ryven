# Vergleich unterschiedlicher Möglichkeiten, einen Flow auszuführen

Beim Flow-Based VP gibt es zwei verschiedene Systeme:

- Reine Dataflows
- Flows mit execution connections

Software wie NodeRed oder NoFlo arbeitet mit reinen Dataflows. Im Falle von NodeRed ermöglicht das sehr einfache Umsetzung von IoT Verbindungen. In der Unreal Engine, sowie in Godot und in pyScript hingegen werden auch execution connections genutzt. Diese ermöglichen eine aktive Ablaufsteuerung (was wann wie oft ausgeführt werden soll), bzw. Kontrollstrukturen. Dies ist der Kontext. Jetzt gibt es allerdings verschiedene Wege, die Datenübertragungen bei passiven Nodes (bei Dataflows existieren einfach nur passive Nodes, alle mit execution inputs und output sind aktiv) umzusetzen.

## Update-Laufrichtung Durch Änderung Rechts

Wenn bei NodeRed sich etwas ändert und dadurch eine connection getriggert wird, wird dieses event von jeder getriggerten Node verarbeitet und anschließend an die nächste weitergegeben. Die Laufrichting der Event-Weitergabe für passive Nodes ist also nach rechts (es existieren dort nur passive Nodes). Ich habe überlegt, in pyScript etwas ähnliches umzusetzen, also dass alle passiven Nodes nach rechts jede _Änderung_ druchpropagieren, bis das Signal an aktive Nodes stößt, die von solch einem data update Event nicht ausgeführt werden, sondern auf ein execution input Signal warten. Dies hätte den Vorteil, dass jede Änderung von Variablen etc. direkt überall durchpropagiert wird und die Ausführung der aktiven Nodes sehr schnell wäre, da die passiven Nodes deren output Werte genutzt werden, nur diese zurückgeben würden und nichts mehr ausführen müssten. 

Dies hat zwei Nachteile:

- Das setzen einer Variable z.B. würde an sehr vielen Stellen im Flow zu riesigen unnötigen Neuberechnungen führen, wenn große passive Nodenetze von dieser Variable abhängen.
- Nodes, die passiv sind aber nicht von input update Events abhängen, können nicht existieren. Der output value einer random Node, die einfach nur eine random Float zwischen 0 und 1 zurückgibt (und keine inputs hat), könnte niemals gesetzt werden, da nicht klar ist wann. Dies ist nur klar, wenn die Node ebenfalls ein Event erhält, wenn der output value von einer anderen Node angefordert wird. Dies wäre aber die gegenteilige Laufrichtung (also Datenüberlieferung durch _Anfrage_ nach links) und damit nicht mit der oberen Version kosequent vereinbar - es sind unterschiedliche Prozesse.

## Update-Laufrichtung Durch Anfrage Links

Es existiert jedoch eben auch die gegenteilige Möglichkeit, die genannte Probleme nicht hätte. Also jede Datenüberlieferung durch **Anfrage** nach links. Eine passive Node wird dann also erst ausgeführt, wenn ein output Wert von einer anderen Node angefordert wird. Dieses output update Event würde dann nach links weitergegeben, da diese passive Node ja eventuell von anderen an die inputs angeschlossenen abhängt. Dies hat hingegen den Nachteil, dass jede Anforderung von output Werten zu einer vollständigen Neuberechnung dieser führen würde (nur jetzt nicht mehr auf Änderung einer Komponente hin, sondern auf Anfrage). Allerdings ist dies deutlich vereinbarer mit der Idee execution connections zu haben, da diese quasi suggerieren, dass wenn ein Wert sich nicht ändert, dieser einfach _aktiv_ in einer Variable zwischengespeichert werden sollte, sodass dieser nur noch von der Variable wiederverwendet werden muss ohne ihn unnötiger Weise neu zu berechnen.

## Lösung

Um die Einheitlichkeit zu wahren, musste ich mich für die zweite Version entscheiden. Da Nodes, die völlig unabhängig von allem auf Anforderung daten generieren und zurückgeben können, möglich sein sollen und das Konzept sehr viel vereinbarer mit dem System ist.

## Ursprüngliche Herangehensweise

Ursprünglich hatte ich eine andere, überaus interessante Umsetzung implementiert. Die Idee war, dass ich pyScript so intelligent macht, dass es selbst merkt, wenn Nodes unnötiger Weise zur Neuberechnung angehalten werden, und in diesem Falle einfach den bereits berechneten Wert zurückgibt. Dies würde ermöglichen, dass man sich keine Gedanken über das Setzen von solchen temorären Variablen machen muss, sondern einfach die Outputs der passiven Nodes nutzen könnte (was auch noch zentrale Vorteile hätte). Diese System funktioniert prinzipiell auch, das Problem ist, dass pyScript dadurch sehr langsam wird. Man kann dieses System benutzen, aber es ist nicht der Standard.

Umgesetzt habe ich das mit Execution-IDs, wie folgt.