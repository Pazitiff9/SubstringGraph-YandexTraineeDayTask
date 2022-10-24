# SubstringGraph-YandexTraineeDayTask
# ЗАДАНИЕ:
Антон стажируется в группе обработки комментариев и отзывов. Для проверки гипотезы об автоматической генерации текстов Антон должен построить граф подстрок существующих текстов.
 
Антон берет все имеющиеся у него слова и действует следующим образом:
    слово S=s1s2…sn−1sn образует n−2 слова длины 3: w1=s1s2s3, w2=s2s3s4, w3=s3s4s5 …wn−2=sn−2sn−1sn;
    если для какого-то из слов wi еще нет вершины в графе, то она создается;
    для каждой пары слов (wi,wi+1) добавляется ориентированное ребро веса 1, или увеличивается вес существующего ребра на 1.
 
Таким образом получается граф G с v вершинами и e ориентированными ребрами. Между некоторыми вершинами может быть несколько дуг (от a к b и от b к a).
По заданному набору слов помогите Антону найти количество вершин в графе и вывести ориентированные ребра между вершинами.
 
Формат ввода
В первой строке записано одно целое число T (1≤T≤40000) — количество слов, имеющихся у Антона.
В каждой из T следующих строк записано одно слово Si (4≤|Si|≤30). Все слова состоят из строчных букв английского алфавита.

Формат вывода
В первой строке выведите количество вершин v в графе G.
Во второй строке выведите количество пар вершин e, между которыми есть ориентированные ребра.
В каждой из следующих e строк выведите слово ws, соответствующее началу ребра, затем слово wf, соответствующее концу ребра, и вес ориентированного ребра из вершины ws в wf.
Ребра вы можете перечислить в произвольном порядке.
