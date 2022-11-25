# -*- coding: utf-8 -*-
"""
Created on Tue Nov 30 21:24:41 2021

@author: rober
"""

import random

# Functions ------------------------------------------------------------------

# function for counting correct answers, following correct answer

def correct_answer_count_add_one(filename="correct_answer_counter.dat"):
    with open(filename, "a+") as f:
        f.seek(0)
        val = int(f.read() or 0) + 1
        f.seek(0)
        f.truncate()
        f.write(str(val))
        return val
    
# function for counting correct answers, following incorrect answer

def correct_answer_count_add_zero(filename="correct_answer_counter.dat"):
    with open(filename, "a+") as f:
        f.seek(0)
        val = int(f.read() or 0) + 0
        f.seek(0)
        f.truncate()
        f.write(str(val))
        return val

# function for counting total answers

def total_answer_count(filename="total_answer_counter.dat"):
    with open(filename, "a+") as f:
        f.seek(0)
        val = int(f.read() or 0) + 1
        f.seek(0)
        f.truncate()
        f.write(str(val))
        return val
    


# Conjugation dictionaries ---------------------------------------------------

# English dictionaries do not contain the French literary tenses

# French dicts ----------------------------------------------------------

dict_etre = {'present' : {'je' : 'suis',
                          'tu' : 'es',
                          'il' : 'est',
                          'nous' : 'sommes',
                          'vous' : 'êtes',
                          'ils' : 'sont'},
             'imperfect' : {'je' : 'étais',
                          'tu' : 'étais',
                          'il' : 'était',
                          'nous' : 'étions',
                          'vous' : 'étiez',
                          'ils' : 'étaient'},
             'future' : {'je' : 'serai',
                          'tu' : 'seras',
                          'il' : 'sera',
                          'nous' : 'serons',
                          'vous' : 'serez',
                          'ils' : 'seront'},
             'conditional' : {'je' : 'serais',
                          'tu' : 'serais',
                          'il' : 'serait',
                          'nous' : 'serions',
                          'vous' : 'seriez',
                          'ils' : 'seraient'},
             'subjunctive' : {'je' : 'sois',
                          'tu' : 'sois',
                          'il' : 'soit',
                          'nous' : 'soyons',
                          'vous' : 'soyez',
                          'ils' : 'soient'},
             'imperfect subj.' : {'je' : 'fusse',
                          'tu' : 'fusses',
                          'il' : 'fût',
                          'nous' : 'fussions',
                          'vous' : 'fussiez',
                          'ils' : 'fussent'},
             'passe compose' : {'je' : 'ai été',
                          'tu' : 'as été',
                          'il' : 'a été',
                          'nous' : 'avons été',
                          'vous' : 'avez été',
                          'ils' : 'ont été'},
             'past perfect' : {'je' : 'avais été',
                          'tu' : 'avais été',
                         'il' : 'avait été',
                          'nous' : 'avions été',
                          'vous' : 'aviez été',
                          'ils' : 'avaient été'},
             'future perfect' : {'je' : 'aurai été',
                          'tu' : 'auras été',
                          'il' : 'aura été',
                          'nous' : 'aurons été',
                          'vous' : 'aurez été',
                          'ils' : 'auront été'},
             'past conditional' : {'je' : 'aurais été',
                          'tu' : 'aurais été',
                          'il' : 'aurait été',
                          'nous' : 'aurions été',
                          'vous' : 'auriez été',
                          'ils' : 'auraient été'},
             'past subjunctive' : {'je' : 'aie été',
                          'tu' : 'aies été',
                          'il' : 'ait été',
                          'nous' : 'ayons été',
                          'vous' : 'ayez été',
                          'ils' : 'aient été'},
             'pluperfect subj.' : {'je' : 'eusse été',
                          'tu' : 'eusses été',
                          'il' : 'eût été',
                          'nous' : 'eussions été',
                          'vous' : 'eussiez été',
                          'ils' : 'eussent été'},
             'passe simple' : {'je' : 'fus',
                          'tu' : 'fus',
                          'il' : 'fut',
                          'nous' : 'fûmes',
                          'vous' : 'fûtes',
                          'ils' : 'furent'},
             'past anterior' : {'je' : 'eus été',
                          'tu' : 'eus été',
                          'il' : 'eut été',
                          'nous' : 'eûmes été',
                          'vous' : 'eûtes été',
                          'ils' : 'eurent été'}
             }

dict_avoir = {'present' : {'je' : 'ai',
                          'tu' : 'as',
                          'il' : 'a',
                          'nous' : 'avons',
                          'vous' : 'avez',
                          'ils' : 'ont'},
             'imperfect' : {'je' : 'avais',
                          'tu' : 'avais',
                          'il' : 'avait',
                          'nous' : 'avions',
                          'vous' : 'aviez',
                          'ils' : 'avaient'},
             'future' : {'je' : 'aurai',
                          'tu' : 'auras',
                          'il' : 'aura',
                          'nous' : 'aurons',
                          'vous' : 'aurez',
                          'ils' : 'auront'},
             'conditional' : {'je' : 'aurais',
                          'tu' : 'aurais',
                          'il' : 'aurait',
                          'nous' : 'aurions',
                          'vous' : 'auriez',
                          'ils' : 'auraient'},
             'subjunctive' : {'je' : 'aie',
                          'tu' : 'aies',
                          'il' : 'ait',
                          'nous' : 'ayons',
                          'vous' : 'ayez',
                          'ils' : 'aient'},
             'imperfect subj.' : {'je' : 'eusse',
                          'tu' : 'eusses',
                          'il' : 'eût',
                          'nous' : 'eussions',
                          'vous' : 'eussiez',
                          'ils' : 'eussent'},
             'passe compose' : {'je' : 'ai eu',
                          'tu' : 'as eu',
                          'il' : 'a eu',
                          'nous' : 'avons eu',
                          'vous' : 'avez eu',
                          'ils' : 'ont eu'},
             'past perfect' : {'je' : 'avais eu',
                          'tu' : 'avais eu',
                          'il' : 'avait eu',
                          'nous' : 'avions eu',
                          'vous' : 'aviez eu',
                          'ils' : 'avaient eu'},
             'future perfect' : {'je' : 'aurai eu',
                          'tu' : 'auras eu',
                          'il' : 'aura eu',
                          'nous' : 'aurons eu',
                          'vous' : 'aurez eu',
                          'ils' : 'auront eu'},
             'past conditional' : {'je' : 'aurais eu',
                          'tu' : 'aurais eu',
                          'il' : 'aurait eu',
                          'nous' : 'aurions eu',
                          'vous' : 'auriez eu',
                          'ils' : 'auraient eu'},
             'past subjunctive' : {'je' : 'aie eu',
                          'tu' : 'aies eu',
                          'il' : 'ait eu',
                          'nous' : 'ayons eu',
                          'vous' : 'ayez eu',
                          'ils' : 'aient eu'},
             'pluperfect subj.' : {'je' : 'eusse eu',
                          'tu' : 'eusses eu',
                          'il' : 'eût eu',
                          'nous' : 'eussions eu',
                          'vous' : 'eussiez eu',
                          'ils' : 'eussent eu'},
             'passe simple' : {'je' : 'eus',
                          'tu' : 'eus',
                          'il' : 'eut',
                          'nous' : 'eûmes',
                          'vous' : 'eûtes',
                          'ils' : 'eurent'},
             'past anterior' : {'je' : 'eus eu',
                          'tu' : 'eus eu',
                          'il' : 'eut eu',
                          'nous' : 'eûmes eu',
                          'vous' : 'eûtes eu',
                          'ils' : 'eurent eu'}
             }


dict_parler = {'present' : {'je' : 'parle',
                          'tu' : 'parles',
                          'il' : 'parle',
                          'nous' : 'parlons',
                          'vous' : 'parlez',
                          'ils' : 'parlent'},
             'imperfect' : {'je' : 'parlais',
                          'tu' : 'parlais',
                          'il' : 'parlait',
                          'nous' : 'parlions',
                          'vous' : 'parliez',
                          'ils' : 'parlaient'},
             'future' : {'je' : 'parlerai',
                          'tu' : 'parleras',
                          'il' : 'parlera',
                          'nous' : 'parlerons',
                          'vous' : 'parlerez',
                          'ils' : 'parleront'},
             'conditional' : {'je' : 'parlerais',
                          'tu' : 'parlerais',
                          'il' : 'parlerait',
                          'nous' : 'parlerions',
                          'vous' : 'parleriez',
                          'ils' : 'parleraient'},
             'subjunctive' : {'je' : 'parle',
                          'tu' : 'parles',
                          'il' : 'parle',
                          'nous' : 'parlions',
                          'vous' : 'parliez',
                          'ils' : 'parlent'},
             'imperfect subj.' : {'je' : 'parlasse',
                          'tu' : 'parlasses',
                          'il' : 'parlât',
                          'nous' : 'parlassions',
                          'vous' : 'parlassiez',
                          'ils' : 'parlassent'},
             'passe compose' : {'je' : 'ai parlé',
                          'tu' : 'as parlé',
                          'il' : 'a parlé',
                          'nous' : 'avons parlé',
                          'vous' : 'avez parlé',
                          'ils' : 'ont parlé'},
             'past perfect' : {'je' : 'avais parlé',
                          'tu' : 'avais parlé',
                          'il' : 'avait parlé',
                          'nous' : 'avions parlé',
                          'vous' : 'aviez parlé',
                          'ils' : 'avaient parlé'},
             'future perfect' : {'je' : 'aurai parlé',
                          'tu' : 'auras parlé',
                          'il' : 'aura parlé',
                          'nous' : 'aurons parlé',
                          'vous' : 'aurez parlé',
                          'ils' : 'auront parlé'},
             'past conditional' : {'je' : 'aurais parlé',
                          'tu' : 'aurais parlé',
                          'il' : 'aurait parlé',
                          'nous' : 'aurions parlé',
                          'vous' : 'auriez parlé',
                          'ils' : 'auraient parlé'},
             'past subjunctive' : {'je' : 'aie parlé',
                          'tu' : 'aies parlé',
                          'il' : 'ait parlé',
                          'nous' : 'ayons parlé',
                          'vous' : 'ayez parlé',
                          'ils' : 'aient parlé'},
             'pluperfect subj.' : {'je' : 'eusse parlé',
                          'tu' : 'eusses parlé',
                         'il' : 'eût parlé',
                          'nous' : 'eussions parlé',
                          'vous' : 'eussiez parlé',
                          'ils' : 'eussent parlé'},
             'passe simple' : {'je' : 'parlai',
                          'tu' : 'parlas',
                          'il' : 'parla',
                          'nous' : 'parlâmes',
                          'vous' : 'parlâtes',
                          'ils' : 'parlèrent'},
             'past anterior' : {'je' : 'eus parlé',
                          'tu' : 'eus parlé',
                          'il' : 'eut parlé',
                          'nous' : 'eûmes parlé',
                          'vous' : 'eûtes parlé',
                          'ils' : 'eurent parlé'}
             }

dict_attendre = {'present' : {'je' : 'attends',
                          'tu' : 'attends',
                          'il' : 'attend',
                          'nous' : 'attendons',
                          'vous' : 'attendez',
                          'ils' : 'attendent'},
             'imperfect' : {'je' : 'attendais',
                          'tu' : 'attendais',
                          'il' : 'attendait',
                          'nous' : 'attendions',
                          'vous' : 'attendiez',
                          'ils' : 'attendaient'},
             'future' : {'je' : 'attendrai',
                          'tu' : 'attendras',
                          'il' : 'attendra',
                          'nous' : 'attendrons',
                          'vous' : 'attendrez',
                          'ils' : 'attendront'},
             'conditional' : {'je' : 'attendrais',
                          'tu' : 'attendrais',
                          'il' : 'attendrait',
                          'nous' : 'attendrions',
                          'vous' : 'attendriez',
                          'ils' : 'attendraient'},
             'subjunctive' : {'je' : 'attende',
                          'tu' : 'attendes',
                          'il' : 'attende',
                          'nous' : 'attendions',
                          'vous' : 'attendiez',
                          'ils' : 'attendent'},
             'imperfect subj.' : {'je' : 'attendisse',
                          'tu' : 'attendisses',
                          'il' : 'attendît',
                          'nous' : 'attendissions',
                          'vous' : 'attendissiez',
                          'ils' : 'attendissent'},
             'passe compose' : {'je' : 'ai attendu',
                          'tu' : 'as attendu',
                          'il' : 'a attendu',
                          'nous' : 'avons attendu',
                          'vous' : 'avez attendu',
                          'ils' : 'ont attendu'},
             'past perfect' : {'je' : 'avais attendu',
                          'tu' : 'avais attendu',
                          'il' : 'avait attendu',
                          'nous' : 'avions attendu',
                          'vous' : 'aviez attendu',
                          'ils' : 'avaient attendu'},
             'future perfect' : {'je' : 'aurai attendu',
                          'tu' : 'auras attendu',
                          'il' : 'aura attendu',
                          'nous' : 'aurons attendu',
                          'vous' : 'aurez attendu',
                          'ils' : 'auront attendu'},
             'past conditional' : {'je' : 'aurais attendu',
                          'tu' : 'aurais attendu',
                          'il' : 'aurait attendu',
                          'nous' : 'aurions attendu',
                          'vous' : 'auriez attendu',
                          'ils' : 'auraient attendu'},
             'past subjunctive' : {'je' : 'aie attendu',
                          'tu' : 'aies attendu',
                          'il' : 'ait attendu',
                          'nous' : 'ayons attendu',
                          'vous' : 'ayez attendu',
                          'ils' : 'aient attendu'},
             'pluperfect subj.' : {'je' : 'eusse attendu',
                          'tu' : 'eusses attendu',
                          'il' : 'eût attendu',
                          'nous' : 'eussions attendu',
                          'vous' : 'eussiez attendu',
                          'ils' : 'eussent attendu'},
             'passe simple' : {'je' : 'attendis',
                          'tu' : 'attendis',
                          'il' : 'attendit',
                          'nous' : 'attendîmes',
                          'vous' : 'attendîtes',
                          'ils' : 'attendirent'},
             'past anterior' : {'je' : 'eus attendu',
                          'tu' : 'eus attendu',
                          'il' : 'eut attendu',
                          'nous' : 'eûmes attendu',
                          'vous' : 'eûtes attendu',
                          'ils' : 'eurent attendu'}
             }

dict_choisir = {'present' : {'je' : 'choisis',
                          'tu' : 'choisis',
                          'il' : 'choisit',
                          'nous' : 'choisissons',
                          'vous' : 'choisissez',
                          'ils' : 'choisissent'},
             'imperfect' : {'je' : 'choisissais',
                          'tu' : 'choisissais',
                          'il' : 'choisissait',
                          'nous' : 'choisissions',
                          'vous' : 'choisissiez',
                          'ils' : 'choisissaient'},
             'future' : {'je' : 'choisirai',
                          'tu' : 'choisiras',
                          'il' : 'choisira',
                          'nous' : 'choisirons',
                          'vous' : 'choisirez',
                          'ils' : 'choisiront'},
             'conditional' : {'je' : 'choisirais',
                          'tu' : 'choisirais',
                          'il' : 'choisirait',
                          'nous' : 'choisirions',
                          'vous' : 'choisiriez',
                          'ils' : 'choisiraient'},
             'subjunctive' : {'je' : 'choisisse',
                          'tu' : 'choisisses',
                          'il' : 'choisisse',
                          'nous' : 'choisissions',
                          'vous' : 'choisissiez',
                          'ils' : 'choisissent'},
             'imperfect subj.' : {'je' : 'choisisse',
                          'tu' : 'choisisses',
                          'il' : 'choisît',
                          'nous' : 'choisissions',
                          'vous' : 'choisissiez',
                          'ils' : 'choisissent'},
             'passe compose' : {'je' : 'ai choisi',
                          'tu' : 'as choisi',
                          'il' : 'a choisi',
                          'nous' : 'avons choisi',
                          'vous' : 'avez choisi',
                          'ils' : 'ont choisi'},
             'past perfect' : {'je' : 'avais choisi',
                          'tu' : 'avais choisi',
                          'il' : 'avait choisi',
                          'nous' : 'avions choisi',
                          'vous' : 'aviez choisi',
                          'ils' : 'avaient choisi'},
             'future perfect' : {'je' : 'aurai choisi',
                          'tu' : 'auras choisi',
                          'il' : 'aura choisi',
                          'nous' : 'aurons choisi',
                          'vous' : 'aurez choisi',
                          'ils' : 'auront choisi'},
             'past conditional' : {'je' : 'aurais choisi',
                          'tu' : 'aurais choisi',
                          'il' : 'aurait choisi',
                          'nous' : 'aurions choisi',
                          'vous' : 'auriez choisi',
                          'ils' : 'auraient choisi'},
             'past subjunctive' : {'je' : 'aie choisi',
                          'tu' : 'aies choisi',
                          'il' : 'ait choisi',
                          'nous' : 'ayons choisi',
                          'vous' : 'ayez choisi',
                          'ils' : 'aient choisi'},
             'pluperfect subj.' : {'je' : 'eusse choisi',
                          'tu' : 'eusses choisi',
                          'il' : 'eût choisi',
                          'nous' : 'eussions choisi',
                          'vous' : 'eussiez choisi',
                          'ils' : 'eussent choisi'},
             'passe simple' : {'je' : 'choisis',
                          'tu' : 'choisis',
                          'il' : 'choisit',
                          'nous' : 'choisîmes',
                          'vous' : 'choisîtes',
                          'ils' : 'choisirent'},
             'past anterior' : {'je' : 'eus choisi',
                          'tu' : 'eus choisi',
                          'il' : 'eut choisi',
                          'nous' : 'eûmes choisi',
                          'vous' : 'eûtes choisi',
                          'ils' : 'eurent choisi'}
             }

dict_aller = {'present' : {'je' : 'vais',
                          'tu' : 'vas',
                          'il' : 'va',
                          'nous' : 'allons',
                          'vous' : 'allez',
                          'ils' : 'vont'},
             'imperfect' : {'je' : 'allais',
                          'tu' : 'allais',
                          'il' : 'allait',
                          'nous' : 'allions',
                          'vous' : 'alliez',
                          'ils' : 'allaient'},
             'future' : {'je' : 'irai',
                          'tu' : 'iras',
                          'il' : 'ira',
                          'nous' : 'irons',
                          'vous' : 'irez',
                          'ils' : 'iront'},
             'conditional' : {'je' : 'irais',
                          'tu' : 'irais',
                          'il' : 'irait',
                          'nous' : 'irions',
                          'vous' : 'iriez',
                          'ils' : 'iraient'},
             'subjunctive' : {'je' : 'aille',
                          'tu' : 'ailles',
                          'il' : 'aille',
                          'nous' : 'allions',
                          'vous' : 'alliez',
                          'ils' : 'aillent'},
             'imperfect subj.' : {'je' : 'allasse',
                          'tu' : 'allasses',
                          'il' : 'allât',
                          'nous' : 'allassions',
                          'vous' : 'allassiez',
                          'ils' : 'allassent'},
             'passe compose' : {'je' : 'suis allé',
                          'tu' : 'es allé',
                          'il' : 'est allé',
                          'nous' : 'sommes allés',
                          'vous' : 'êtes allé(s)',
                          'ils' : 'sont allés'},
             'past perfect' : {'je' : 'étais allé',
                          'tu' : 'étais allé',
                          'il' : 'était allé',
                          'nous' : 'étions allés',
                          'vous' : 'étiez allé(s)',
                          'ils' : 'étaient allés'},
             'future perfect' : {'je' : 'serai allé',
                          'tu' : 'seras allé',
                          'il' : 'sera allé',
                          'nous' : 'serons allés',
                          'vous' : 'serez allé(s)',
                          'ils' : 'seront allés'},
             'past conditional' : {'je' : 'serais allé',
                          'tu' : 'serais allé',
                          'il' : 'serait allé',
                          'nous' : 'serions allés',
                          'vous' : 'seriez allé(s)',
                          'ils' : 'seraient allés'},
             'past subjunctive' : {'je' : 'sois allé',
                          'tu' : 'sois allé',
                          'il' : 'soit allé',
                          'nous' : 'soyons allés',
                          'vous' : 'soyez allé(s)',
                          'ils' : 'soient allés'},
             'pluperfect subj.' : {'je' : 'fusse allé',
                          'tu' : 'fusses allé',
                          'il' : 'fût allé',
                          'nous' : 'fussions allés',
                          'vous' : 'fussiez allé(s)',
                          'ils' : 'fussent allés'},
             'passe simple' : {'je' : 'allai',
                          'tu' : 'allas',
                          'il' : 'alla',
                          'nous' : 'allâmes',
                          'vous' : 'allâtes',
                          'ils' : 'allèrent'},
             'past anterior' : {'je' : 'fus allé',
                          'tu' : 'fus allé',
                          'il' : 'fut allé',
                          'nous' : 'fûmes allés',
                          'vous' : 'fûtes allé(s)',
                          'ils' : 'furent allés'}
             }

dict_descendre = {'present' : {'je' : 'descends',
                          'tu' : 'descends',
                          'il' : 'descend',
                          'nous' : 'descendons',
                          'vous' : 'descendez',
                          'ils' : 'descendent'},
             'imperfect' : {'je' : 'descendais',
                          'tu' : 'descendais',
                          'il' : 'descendait',
                          'nous' : 'descendions',
                          'vous' : 'descendiez',
                          'ils' : 'descendaient'},
             'future' : {'je' : 'descendrai',
                          'tu' : 'descendras',
                          'il' : 'descendra',
                          'nous' : 'descendrons',
                          'vous' : 'descendrez',
                          'ils' : 'descendront'},
             'conditional' : {'je' : 'descendrais',
                          'tu' : 'descendrais',
                          'il' : 'descendrait',
                          'nous' : 'descendrions',
                          'vous' : 'descendriez',
                          'ils' : 'descendraient'},
             'subjunctive' : {'je' : 'descende',
                          'tu' : 'descendes',
                          'il' : 'descende',
                          'nous' : 'descendions',
                          'vous' : 'descendiez',
                          'ils' : 'descendent'},
             'imperfect subj.' : {'je' : 'descendisse',
                          'tu' : 'descendisses',
                          'il' : 'descendît',
                          'nous' : 'descendissions',
                          'vous' : 'descendissiez',
                          'ils' : 'descendissent'},
             'passe compose' : {'je' : 'suis descendu*',
                          'tu' : 'es descendu',
                          'il' : 'est descendu',
                          'nous' : 'sommes descendus',
                          'vous' : 'êtes descendu(s)',
                          'ils' : 'sont descendus'},
             'past perfect' : {'je' : 'étais descendu',
                          'tu' : 'étais descendu',
                          'il' : 'était descendu',
                          'nous' : 'étions descendus',
                          'vous' : 'étiez descendu(s)',
                          'ils' : 'étaient descendus'},
             'future perfect' : {'je' : 'serai descendu',
                          'tu' : 'seras descendu',
                          'il' : 'sera descendu',
                          'nous' : 'serons descendus',
                          'vous' : 'serez descendu(s)',
                          'ils' : 'seront descendus'},
             'past conditional' : {'je' : 'serais descendu',
                          'tu' : 'serais descendu',
                          'il' : 'serait descendu',
                          'nous' : 'serions descendus',
                          'vous' : 'seriez descendu(s)',
                          'ils' : 'seraient descendus'},
             'past subjunctive' : {'je' : 'sois descendu',
                          'tu' : 'sois descendu',
                          'il' : 'soit descendu',
                          'nous' : 'soyons descendus',
                          'vous' : 'soyez descendu(s)',
                          'ils' : 'soient descendus'},
             'pluperfect subj.' : {'je' : 'fusse descendu',
                          'tu' : 'fusses descendu',
                          'il' : 'fût descendu',
                          'nous' : 'fussions descendus',
                          'vous' : 'fussiez descendu(s)',
                          'ils' : 'fussent descendus'},
             'passe simple' : {'je' : 'descendis',
                          'tu' : 'descendis',
                          'il' : 'descendit',
                          'nous' : 'descendîmes',
                          'vous' : 'descendîtes',
                          'ils' : 'descendirent'},
             'past anterior' : {'je' : 'fus descendu',
                          'tu' : 'fus descendu',
                          'il' : 'fut descendu',
                          'nous' : 'fûmes descendus',
                          'vous' : 'fûtes descendu(s)',
                          'ils' : 'furent descendus'}
             }

dict_venir = {'present' : {'je' : 'viens',
                          'tu' : 'viens',
                          'il' : 'vient',
                          'nous' : 'venons',
                          'vous' : 'venez',
                          'ils' : 'viennent'},
             'imperfect' : {'je' : 'venais',
                          'tu' : 'venais',
                          'il' : 'venait',
                          'nous' : 'venions',
                          'vous' : 'veniez',
                          'ils' : 'venaient'},
             'future' : {'je' : 'viendrai',
                          'tu' : 'viendras',
                          'il' : 'viendra',
                          'nous' : 'viendrons',
                          'vous' : 'viendrez',
                          'ils' : 'viendront'},
             'conditional' : {'je' : 'viendrais',
                          'tu' : 'viendrais',
                          'il' : 'viendrait',
                          'nous' : 'viendrions',
                          'vous' : 'viendriez',
                          'ils' : 'viendraient'},
             'subjunctive' : {'je' : 'vienne',
                          'tu' : 'viennes',
                          'il' : 'vienne',
                          'nous' : 'venions',
                          'vous' : 'veniez',
                          'ils' : 'viennent'},
             'imperfect subj.' : {'je' : 'vinsse',
                          'tu' : 'vinsses',
                          'il' : 'vînt',
                          'nous' : 'vinssions',
                          'vous' : 'vinssiez',
                          'ils' : 'vinssent'},
             'passe compose' : {'je' : 'suis venu',
                          'tu' : 'es venu',
                          'il' : 'est venu',
                          'nous' : 'sommes venus',
                          'vous' : 'êtes venu(s)',
                          'ils' : 'sont venus'},
             'past perfect' : {'je' : 'étais venu',
                          'tu' : 'étais venu',
                          'il' : 'était venu',
                          'nous' : 'étions venus',
                          'vous' : 'étiez venu(s)',
                          'ils' : 'étaient venus'},
             'future perfect' : {'je' : 'serai venu',
                          'tu' : 'seras venu',
                          'il' : 'sera venu',
                          'nous' : 'serons venus',
                          'vous' : 'serez venu(s)',
                          'ils' : 'seront venus'},
             'past conditional' : {'je' : 'serais venu',
                          'tu' : 'serais venu',
                          'il' : 'serait venu',
                          'nous' : 'serions venus',
                          'vous' : 'seriez venu(s)',
                          'ils' : 'seraient venus'},
             'past subjunctive' : {'je' : 'sois venu',
                          'tu' : 'sois venu',
                          'il' : 'soit venu',
                          'nous' : 'soyons venus',
                          'vous' : 'soyez venu(s)',
                          'ils' : 'soient venus'},
             'pluperfect subj.' : {'je' : 'fusse venu',
                          'tu' : 'fusses venu',
                          'il' : 'fût venu',
                          'nous' : 'fussions venus',
                          'vous' : 'fussiez venu(s)',
                          'ils' : 'fussent venus'},
             'passe simple' : {'je' : 'vins',
                          'tu' : 'vins',
                          'il' : 'vint',
                          'nous' : 'vînmes',
                          'vous' : 'vîntes',
                          'ils' : 'vinrent'},
             'past anterior' : {'je' : 'fus venu',
                          'tu' : 'fus venu',
                          'il' : 'fut venu',
                          'nous' : 'fûmes venus',
                          'vous' : 'fûtes venu(s)',
                          'ils' : 'furent venus'}
             }


# English dicts ---------------------------------------------------------

dict_to_be = {'present' : {'I' : 'am',
                          'you' : 'are',
                          'he' : 'is',
                          'we' : 'are',
                          'you' : 'are',
                          'they' : 'are',},
             'imperfect' : {'I' : 'was',
                          'you' : 'were',
                          'he' : 'was',
                          'we' : 'were',
                          'you' : 'were',
                          'they' : 'were',},
             'future' : {'I' : 'will be',
                          'you' : 'will be',
                          'he' : 'will be',
                          'we' : 'will be',
                          'you' : 'will be',
                          'they' : 'will be',},
             'conditional' : {'I' : 'would be',
                          'you' : 'would be',
                          'he' : 'would be',
                          'we' : 'would be',
                          'you' : 'would be',
                          'they' : 'would be',},
             'subjunctive' : {'I' : 'were',
                          'you' : 'were',
                          'he' : 'were',
                          'we' : 'were',
                          'you' : 'were',
                          'they' : 'were',},
             'passe compose' : {'I' : 'have been',
                          'you' : 'have been',
                          'he' : 'has been',
                          'we' : 'have been',
                          'you' : 'have been',
                          'they' : 'have been',},
             'past perfect' : {'I' : 'had been',
                          'you' : 'had been',
                          'he' : 'had been',
                          'we' : 'had been',
                          'you' : 'had been',
                          'they' : 'had been',},
             'future perfect' : {'I' : 'will have been',
                          'you' : 'will have been',
                          'he' : 'will have been',
                          'we' : 'will have been',
                          'you' : 'will have been',
                          'they' : 'will have been',},
             'past conditional' : {'I' : 'would have been',
                          'you' : 'would have been',
                          'he' : 'would have been',
                          'we' : 'would have been',
                          'you' : 'would have been',
                          'they' : 'would have been'},
             'past subjunctive' : {'I' : 'were',
                          'you' : 'were',
                          'he' : 'were',
                          'we' : 'were',
                          'you' : 'were',
                          'they' : 'were'}
             }

dict_to_have = {'present' : {'I' : 'have',
                          'you' : 'have',
                          'he' : 'has',
                          'we' : 'have',
                          'you' : 'have',
                          'they' : 'have'},
             'imperfect' : {'I' : 'had',
                          'you' : 'had',
                          'he' : 'had',
                          'we' : 'had',
                          'you' : 'had',
                          'they' : 'had'},
             'future' : {'I' : 'will have',
                          'you' : 'will have',
                         'he' : 'will have',
                          'we' : 'will have',
                          'you' : 'will have',
                          'they' : 'will have'},
             'conditional' : {'I' : 'would have',
                          'you' : 'would have',
                          'he' : 'would have',
                          'we' : 'would have',
                          'you' : 'would have',
                          'they' : 'would have'},
             'subjunctive' : {'I' : 'had',
                          'you' : 'had',
                          'he' : 'had',
                          'we' : 'had',
                          'you' : 'had',
                          'they' : 'had'},
             'passe compose' : {'I' : 'have had',
                          'you' : 'have had',
                          'he' : 'has had',
                          'we' : 'have had',
                          'you' : 'have had',
                          'they' : 'have had'},
             'past perfect' : {'I' : 'had had',
                          'you' : 'had had',
                          'he' : 'had had',
                          'we' : 'had had',
                          'you' : 'had had',
                          'they' : 'had had'},
             'future perfect' : {'I' : 'will have had',
                          'you' : 'will have had',
                          'he' : 'will have had',
                          'we' : 'will have had',
                          'you' : 'will have had',
                          'they' : 'will have had'},
             'past conditional' : {'I' : 'would have had',
                          'you' : 'would have had',
                          'he' : 'would have had',
                          'we' : 'would have had',
                          'you' : 'would have had',
                          'they' : 'would have had'},
             'past subjunctive' : {'I' : 'had',
                          'you' : 'had',
                          'he' : 'had',
                          'we' : 'had',
                          'you' : 'had',
                          'they' : 'had'}
             }

dict_to_talk = {'present' : {'I' : 'talk',
                          'you' : 'talk',
                          'he' : 'talks',
                          'we' : 'talk',
                          'you' : 'talk',
                          'they' : 'talk'},
             'imperfect' : {'I' : 'talked',
                          'you' : 'talked',
                          'he' : 'talked',
                          'we' : 'talked',
                          'you' : 'talked',
                          'they' : 'talked'},
             'future' : {'I' : 'will talk',
                          'you' : 'will talk',
                          'he' : 'will talk',
                          'we' : 'will talk',
                          'you' : 'will talk',
                          'they' : 'will talk'},
             'conditional' : {'I' : 'would talk',
                          'you' : 'would talk',
                          'he' : 'would talk',
                          'we' : 'would talk',
                          'you' : 'would talk',
                          'they' : 'would talk'},
             'subjunctive' : {'I' : 'talk',
                          'you' : 'talk',
                          'he' : 'talk',
                          'we' : 'talk',
                          'you' : 'talk',
                          'they' : 'talk'},
             'passe compose' : {'I' : 'have talked',
                          'you' : 'have talked',
                          'he' : 'has talked',
                          'we' : 'have talked',
                          'you' : 'have talked',
                          'they' : 'have talked'},
             'past perfect' : {'I' : 'had talked',
                          'you' : 'had talked',
                          'he' : 'had talked',
                          'we' : 'had talked',
                          'you' : 'had talked',
                          'they' : 'had talked'},
             'future perfect' : {'I' : 'will have talked',
                          'you' : 'will have talked',
                          'he' : 'will have talked',
                          'we' : 'will have talked',
                          'you' : 'will have talked',
                          'they' : 'will have talked'},
             'past conditional' : {'I' : 'would have talked',
                          'you' : 'would have talked',
                          'he' : 'would have talked',
                          'we' : 'would have talked',
                          'you' : 'would have talked',
                          'they' : 'would have talked'},
             'past subjunctive' : {'I' : 'talked',
                          'you' : 'talked',
                          'he' : 'talked',
                          'we' : 'talked',
                          'you' : 'talked',
                          'they' : 'talked'}
             }

dict_to_wait = {'present' : {'I' : 'wait',
                          'you' : 'wait',
                          'he' : 'waits',
                          'we' : 'wait',
                          'you' : 'wait',
                          'they' : 'wait'},
             'imperfect' : {'I' : 'waited',
                         'you' : 'waited',
                          'he' : 'waited',
                          'we' : 'waited',
                          'you' : 'waited',
                          'they' : 'waited'},
             'future' : {'I' : 'will wait',
                          'you' : 'will wait',
                          'he' : 'will wait',
                          'we' : 'will wait',
                          'you' : 'will wait',
                          'they' : 'will wait'},
             'conditional' : {'I' : 'would wait',
                          'you' : 'would wait',
                          'he' : 'would wait',
                          'we' : 'would wait',
                          'you' : 'would wait',
                          'they' : 'would wait'},
             'subjunctive' : {'I' : 'wait',
                          'you' : 'wait',
                          'he' : 'wait',
                          'we' : 'wait',
                          'you' : 'wait',
                          'they' : 'wait'},
             'passe compose' : {'I' : 'have waited',
                          'you' : 'have waited',
                          'he' : 'has waited',
                          'we' : 'have waited',
                          'you' : 'have waited',
                          'they' : 'have waited'},
             'past perfect' : {'I' : 'had waited',
                          'you' : 'had waited',
                          'he' : 'had waited',
                          'we' : 'had waited',
                          'you' : 'had waited',
                          'they' : 'had waited'},
             'future perfect' : {'I' : 'will have waited',
                          'you' : 'will have waited',
                          'he' : 'will have waited',
                          'we' : 'will have waited',
                          'you' : 'will have waited',
                          'they' : 'will have waited'},
             'past conditional' : {'I' : 'would have waited',
                          'you' : 'would have waited',
                          'he' : 'would have waited',
                          'we' : 'would have waited',
                          'you' : 'would have waited',
                          'they' : 'would have waited'},
             'past subjunctive' : {'I' : 'waited',
                          'you' : 'waited',
                          'he' : 'waited',
                          'we' : 'waited',
                          'you' : 'waited',
                          'they' : 'waited'}
             }

dict_to_choose = {'present' : {'I' : 'choose',
                          'you' : 'choose',
                          'he' : 'chooses',
                          'we' : 'choose',
                          'you' : 'choose',
                          'they' : 'choose'},
             'imperfect' : {'I' : 'chose',
                          'you' : 'chose',
                          'he' : 'chose',
                          'we' : 'chose',
                          'you' : 'chose',
                          'they' : 'chose'},
             'future' : {'I' : 'will choose',
                          'you' : 'will choose',
                          'he' : 'will choose',
                          'we' : 'will choose',
                          'you' : 'will choose',
                          'they' : 'will choose'},
             'conditional' : {'I' : 'would choose',
                          'you' : 'would choose',
                          'he' : 'would choose',
                          'we' : 'would choose',
                          'you' : 'would choose',
                          'they' : 'would choose'},
             'subjunctive' : {'I' : 'choose',
                          'you' : 'choose',
                          'he' : 'chooses',
                          'we' : 'choose',
                          'you' : 'choose',
                          'they' : 'choose'},
             'passe compose' : {'I' : 'have chosen',
                          'you' : 'have chosen',
                          'he' : 'has chosen',
                          'we' : 'have chosen',
                          'you' : 'have chosen',
                          'they' : 'have chosen'},
             'past perfect' : {'I' : 'had chosen',
                          'you' : 'had chosen',
                          'he' : 'had chosen',
                          'we' : 'had chosen',
                          'you' : 'had chosen',
                          'they' : 'had chosen'},
             'future perfect' : {'I' : 'will have chosen',
                          'you' : 'will have chosen',
                          'he' : 'will have chosen',
                          'we' : 'will have chosen',
                          'you' : 'will have chosen',
                          'they' : 'will have chosen'},
             'past conditional' : {'I' : 'would have chosen',
                          'you' : 'would have chosen',
                          'he' : 'would have chosen',
                          'we' : 'would have chosen',
                          'you' : 'would have chosen',
                          'they' : 'would have chosen'},
             'past subjunctive' : {'I' : 'chose',
                          'you' : 'chose',
                          'he' : 'chose',
                          'we' : 'chose',
                          'you' : 'chose',
                          'they' : 'chose'}
             }

dict_to_go = {'present' : {'I' : 'go',
                          'you' : 'go',
                          'he' : 'goes',
                          'we' : 'go',
                          'you' : 'go',
                          'they' : 'go'},
             'imperfect' : {'I' : 'went',
                          'you' : 'went',
                          'he' : 'went',
                          'we' : 'went',
                          'you' : 'went',
                          'they' : 'went'},
             'future' : {'I' : 'will go',
                          'you' : 'will go',
                          'he' : 'will go',
                          'we' : 'will go',
                          'you' : 'will go',
                          'they' : 'will go'},
             'conditional' : {'I' : 'would go',
                          'you' : 'would go',
                          'he' : 'would go',
                          'we' : 'would go',
                          'you' : 'would go',
                          'they' : 'would go'},
             'subjunctive' : {'I' : 'go',
                          'you' : 'go',
                          'he' : 'goes',
                          'we' : 'go',
                          'you' : 'go',
                          'they' : 'go'},
             'passe compose' : {'I' : 'have gone',
                          'you' : 'have gone',
                          'he' : 'has gone',
                          'we' : 'have gone',
                          'you' : 'have gone',
                          'they' : 'have gone'},
             'past perfect' : {'I' : 'had gone',
                          'you' : 'had gone',
                          'he' : 'had gone',
                          'we' : 'had gone',
                          'you' : 'had gone',
                          'they' : 'had gone'},
             'future perfect' : {'I' : 'will have gone',
                          'you' : 'will have gone',
                          'he' : 'will have gone',
                          'we' : 'will have gone',
                          'you' : 'will have gone',
                          'they' : 'will have gone'},
             'past conditional' : {'I' : 'would have gone',
                          'you' : 'would have gone',
                          'he' : 'would have gone',
                          'we' : 'would have gone',
                          'you' : 'would have gone',
                          'they' : 'would have gone'},
             'past subjunctive' : {'I' : 'went',
                          'you' : 'went',
                          'he' : 'went',
                          'we' : 'went',
                          'you' : 'went',
                          'they' : 'went'}
             }

dict_to_descend = {'present' : {'I' : 'descend',
                          'you' : 'descend',
                          'he' : 'descends',
                          'we' : 'descend',
                          'you' : 'descend',
                          'they' : 'descend'},
             'imperfect' : {'I' : 'descended',
                          'you' : 'descended',
                          'he' : 'descended',
                          'we' : 'descended',
                          'you' : 'descended',
                          'they' : 'descended'},
             'future' : {'I' : 'will descend',
                          'you' : 'will descend',
                          'he' : 'will descend',
                          'we' : 'will descend',
                          'you' : 'will descend',
                          'they' : 'will descend'},
             'conditional' : {'I' : 'would descend',
                          'you' : 'would descend',
                          'he' : 'would descend',
                          'we' : 'would descend',
                          'you' : 'would descend',
                          'they' : 'would descend'},
             'subjunctive' : {'I' : 'descend',
                          'you' : 'descend',
                          'he' : 'descend',
                          'we' : 'descend',
                          'you' : 'descend',
                          'they' : 'descend'},
             'passe compose' : {'I' : 'have descended',
                          'you' : 'have descended',
                          'he' : 'has descended',
                          'we' : 'have descended',
                          'you' : 'have descended',
                          'they' : 'have descended'},
             'past perfect' : {'I' : 'had descended',
                          'you' : 'had descended',
                          'he' : 'had descended',
                          'we' : 'had descended',
                          'you' : 'had descended',
                          'they' : 'had descended'},
             'future perfect' : {'I' : 'will have descended',
                          'you' : 'will have descended',
                          'he' : 'will have descended',
                          'we' : 'will have descended',
                          'you' : 'will have descended',
                          'they' : 'will have descended'},
             'past conditional' : {'I' : 'would have descended',
                          'you' : 'would have descended',
                          'he' : 'would have descended',
                          'we' : 'would have descended',
                          'you' : 'would have descended',
                          'they' : 'would have descended'},
             'past subjunctive' : {'I' : 'descended',
                          'you' : 'descended',
                          'he' : 'descended',
                          'we' : 'descended',
                          'you' : 'descended',
                          'they' : 'descended'}
             }

dict_to_come = {'present' : {'I' : 'come',
                          'you' : 'come',
                          'he' : 'comes',
                          'we' : 'come',
                          'you' : 'come',
                          'they' : 'come'},
             'imperfect' : {'I' : 'came',
                          'you' : 'came',
                          'he' : 'came',
                          'we' : 'came',
                          'you' : 'came',
                          'they' : 'came'},
             'future' : {'I' : 'will come',
                          'you' : 'will come',
                          'he' : 'will come',
                          'we' : 'will come',
                          'you' : 'will come',
                          'they' : 'will come'},
             'conditional' : {'I' : 'would come',
                          'you' : 'would come',
                          'he' : 'would come',
                          'we' : 'would come',
                          'you' : 'would come',
                          'they' : 'would come'},
             'subjunctive' : {'I' : 'come',
                          'you' : 'come',
                          'he' : 'come',
                          'we' : 'come',
                          'you' : 'come',
                          'they' : 'come'},
             'passe compose' : {'I' : 'have come',
                          'you' : 'have come',
                          'he' : 'has come',
                          'we' : 'have come',
                          'you' : 'have come',
                          'they' : 'have come'},
             'past perfect' : {'I' : 'had come',
                          'you' : 'had come',
                          'he' : 'had come',
                          'we' : 'had come',
                          'you' : 'had come',
                          'they' : 'had come'},
             'future perfect' : {'I' : 'will have come',
                          'you' : 'will have come',
                          'he' : 'will have come',
                          'we' : 'will have come',
                          'you' : 'will have come',
                          'they' : 'will have come'},
             'past conditional' : {'I' : 'would have come',
                          'you' : 'would have come',
                          'he' : 'would have come',
                          'we' : 'would have come',
                          'you' : 'would have come',
                          'they' : 'would have come'},
             'past subjunctive' : {'I' : 'came',
                          'you' : 'came',
                          'he' : 'came',
                          'we' : 'came',
                          'you' : 'came',
                          'they' : 'came'}
             }


# Conjugation lists ----------------------------------------------------------

# Lists contain only the English tenses

# French lists ----------------------------------------------------------

list_etre = [
            ['suis', 'es', 'est', 'sommes', 'êtes', 'sont'],
            ['étais', 'étais', 'était', 'étions', 'étiez', 'étaient'],
            ['serai', 'seras', 'sera', 'serons', 'serez', 'seront'],
            ['serais', 'serais', 'serait', 'serions', 'seriez', 'seraient'],
            ['sois', 'sois', 'soit', 'soyons', 'soyez', 'soient'],
            ['ai été', 'as été', 'a été', 'avons été', 'avez été', 'ont été'],
            ['avais été', 'avais été', 'avait été', 'avions été', 'aviez été', 'avaient été'],
            ['aurai été', 'auras été', 'aura été', 'aurons été', 'aurez été', 'auront été'],
            ['aurais été', 'aurais été', 'aurait été', 'aurions été', 'auriez été', 'auraient été'],
            ['aie été', 'aies été', 'ait été', 'ayons été', 'ayez été', 'aient été'],
            ]

list_avoir = [
            ['ai', 'as', 'a', 'avons', 'avez', 'ont'],
            ['avais', 'avais', 'avait', 'avions', 'aviez', 'avaient'],
            ['aurai', 'auras', 'aura', 'aurons', 'aurez', 'auront'],
            ['aurais', 'aurais', 'aurait', 'aurions', 'auriez', 'auraient'],
            ['aie', 'aies', 'ait', 'ayons', 'ayez', 'aient'],
            ['ai eu', 'as eu', 'a eu', 'avons eu', 'avez eu', 'ont eu'],
            ['avais eu', 'avais eu', 'avait eu', 'avions eu', 'aviez eu', 'avaient eu'],
            ['aurai eu', 'auras eu', 'aura eu', 'aurons eu', 'aurez eu', 'auront eu'],
            ['aurais eu', 'aurais eu', 'aurait eu', 'aurions eu', 'auriez eu', 'auraient eu'],
            ['aie eu', 'aies eu', 'ait eu', 'ayons eu', 'ayez eu', 'aient eu'],
            ]

list_parler = [
            ['parle', 'parles', 'parle', 'parlons', 'parlez', 'parlent'],
            ['parlais', 'parlais', 'parlait', 'parlions', 'parliez', 'parlaient'],
            ['parlerai', 'parleras', 'parlera', 'parlerons', 'parlerez', 'parleront'],
            ['parlerais', 'parlerais', 'parlerait', 'parlerions', 'parleriez', 'parleraient'],
            ['parle', 'parles', 'parle', 'parlions', 'parliez', 'parlent'],
            ['ai parlé', 'as parlé', 'a parlé', 'avons parlé', 'avez parlé', 'ont parlé'],
            ['avais parlé', 'avais parlé', 'avait parlé', 'avions parlé', 'aviez parlé', 'avaient parlé'],
            ['aurai parlé', 'auras parlé', 'aura parlé', 'aurons parlé', 'aurez parlé', 'auront parlé'],
            ['aurais parlé', 'aurais parlé', 'aurait parlé', 'aurions parlé', 'auriez parlé', 'auraient parlé'],
            ['aie parlé', 'aies parlé', 'ait parlé', 'ayons parlé', 'ayez parlé', 'aient parlé'],
            ]

list_attendre = [
            ['attends', 'attends', 'attend', 'attendons', 'attendez', 'attendent'],
            ['attendais', 'attendais', 'attendait', 'attendions', 'attendiez', 'attendaient'],
            ['attendrai', 'attendras', 'attendra', 'attendrons', 'attendrez', 'attendront'],
            ['attendrais', 'attendrais', 'attendrait', 'attendrions', 'attendriez', 'attendraient'],
            ['attende', 'attendes', 'attende', 'attendions', 'attendiez', 'attendent'],
            ['ai attendu', 'as attendu', 'a attendu', 'avons attendu', 'avez attendu', 'ont attendu'],
            ['avais attendu', 'avais attendu', 'avait attendu', 'avions attendu', 'aviez attendu', 'avaient attendu'],
            ['aurai attendu', 'auras attendu', 'aura attendu', 'aurons attendu', 'aurez attendu', 'auront attendu'],
            ['aurais attendu', 'aurais attendu', 'aurait attendu', 'aurions attendu', 'auriez attendu', 'auraient attendu'],
            ['aie attendu', 'aies attendu', 'ait attendu', 'ayons attendu', 'ayez attendu', 'aient attendu'],
            ]

list_choisir = [
            ['choisis', 'choisis', 'choisit', 'choisissons', 'choisissez', 'choisissent'],
            ['choisissais', 'choisissais', 'choisissait', 'choisissions', 'choisissiez', 'choisissaient'],
            ['choisirai', 'choisiras', 'choisira', 'choisirons', 'choisirez', 'choisiront'],
            ['choisirais', 'choisirais', 'choisirait', 'choisirions', 'choisiriez', 'choisiraient'],
            ['choisisse', 'choisisses', 'choisisse', 'choisissions', 'choisissiez', 'choisissent'],
            ['ai choisi', 'as choisi', 'a choisi', 'avons choisi', 'avez choisi', 'ont choisi'],
            ['avais choisi', 'avais choisi', 'avait choisi', 'avions choisi', 'aviez choisi', 'avaient choisi'],
            ['aurai choisi', 'auras choisi', 'aura choisi', 'aurons choisi', 'aurez choisi', 'auront choisi'],
            ['aurais choisi', 'aurais choisi', 'aurait choisi', 'aurions choisi', 'auriez choisi', 'auraient choisi'],
            ['aie choisi', 'aies choisi', 'ait choisi', 'ayons choisi', 'ayez choisi', 'aient choisi'],
            ]

list_aller = [
            ['vais', 'vas', 'va', 'allons', 'allez', 'vont'],
            ['allais', 'allais', 'allait', 'allions', 'alliez', 'allaient'],
            ['irai', 'iras', 'ira', 'irons', 'irez', 'iront'],
            ['irais', 'irais', 'irait', 'irions', 'iriez', 'iraient'],
            ['aille', 'ailles', 'aille', 'allions', 'alliez', 'aillent'],
            ['suis allé', 'es allé', 'est allé', 'sommes allés', 'êtes allé(s)', 'sont allés'],
            ['étais allé', 'étais allé', 'était allé', 'étions allés', 'étiez allé(s)', 'étaient allés'],
            ['serai allé', 'seras allé', 'sera allé', 'serons allés', 'serez allé(s)', 'seront allés'],
            ['serais allé', 'serais allé', 'serait allé', 'serions allés', 'seriez allé(s)', 'seraient allés'],
            ['sois allé', 'sois allé', 'soit allé', 'soyons allés', 'soyez allé(s)', 'soient allés'],
            ]

list_descendre = [
            ['descends', 'descends', 'descend', 'descendons', 'descendez', 'descendent'],
            ['descendais', 'descendais', 'descendait', 'descendions', 'descendiez', 'descendaient'],
            ['descendrai', 'descendras', 'descendra', 'descendrons', 'descendrez', 'descendront'],
            ['descendrais', 'descendrais', 'descendrait', 'descendrions', 'descendriez', 'descendraient'],
            ['descende', 'descendes', 'descende', 'descendions', 'descendiez', 'descendent'],
            ['suis descendu*', 'es descendu', 'est descendu', 'sommes descendus', 'êtes descendu(s)', 'sont descendus'],
            ['étais descendu', 'étais descendu', 'était descendu', 'étions descendus', 'étiez descendu(s)', 'étaient descendus'],
            ['serai descendu', 'seras descendu', 'sera descendu', 'serons descendus', 'serez descendu(s)', 'seront descendus'],
            ['serais descendu', 'serais descendu', 'serait descendu', 'serions descendus', 'seriez descendu(s)', 'seraient descendus'],
            ['sois descendu', 'sois descendu', 'soit descendu', 'soyons descendus', 'soyez descendu(s)', 'soient descendus'],
            ]

list_venir = [
            ['viens', 'viens', 'vient', 'venons', 'venez', 'viennent'],
            ['venais', 'venais', 'venait', 'venions', 'veniez', 'venaient'],
            ['viendrai', 'viendras', 'viendra', 'viendrons', 'viendrez', 'viendront'],
            ['viendrais', 'viendrais', 'viendrait', 'viendrions', 'viendriez', 'viendraient'],
            ['vienne', 'viennes', 'vienne', 'venions', 'veniez', 'viennent'],
            ['suis venu', 'es venu', 'est venu', 'sommes venus', 'êtes venu(s)', 'sont venus'],
            ['étais venu', 'étais venu', 'était venu', 'étions venus', 'étiez venu(s)', 'étaient venus'],
            ['serai venu', 'seras venu', 'sera venu', 'serons venus', 'serez venu(s)', 'seront venus'],
            ['serais venu', 'serais venu', 'serait venu', 'serions venus', 'seriez venu(s)', 'seraient venus'],
            ['sois venu', 'sois venu', 'soit venu', 'soyons venus', 'soyez venu(s)', 'soient venus'],
            ]


# English lists ---------------------------------------------------------

list_to_be = [
             ['am', 'are', 'is', 'are', 'are', 'are'],
             ['was', 'were', 'was', 'were', 'were', 'were'],
             ['will be', 'will be', 'will be', 'will be', 'will be', 'will be'],
             ['would be', 'would be', 'would be', 'would be', 'would be', 'would be'],
             ['were', 'were', 'were', 'were', 'were', 'were'],
             ['have been', 'have been', 'has been', 'have been', 'have been', 'have been'],
             ['had been', 'had been', 'had been', 'had been', 'had been', 'had been'],
             ['will have been', 'will have been', 'will have been', 'will have been', 'will have been', 'will have been'],
             ['would have been', 'would have been', 'would have been', 'would have been', 'would have been', 'would have been'],
             ['were', 'were', 'were', 'were', 'were', 'were']
             ]

list_to_have = [
             ['have', 'have', 'has', 'have', 'have', 'have'],
             ['had', 'had', 'had', 'had', 'had', 'had'],
             ['will have', 'will have', 'will have', 'will have', 'will have', 'will have'],
             ['would have', 'would have', 'would have', 'would have', 'would have', 'would have'],
             ['had', 'had', 'had', 'had', 'had', 'had'],
             ['have had', 'have had', 'has had', 'have had', 'have had', 'have had'],
             ['had had', 'had had', 'had had', 'had had', 'had had', 'had had'],
             ['will have had', 'will have had', 'will have had', 'will have had', 'will have had', 'will have had'],
             ['would have had', 'would have had', 'would have had', 'would have had', 'would have had', 'would have had'],
             ['had', 'had', 'had', 'had', 'had', 'had']
             ]

list_to_talk = [
            ['talk', 'talk', 'talks', 'talk', 'talk', 'talk'],
            ['talked', 'talked', 'talked', 'talked', 'talked', 'talked'],
            ['will talk', 'will talk', 'will talk', 'will talk', 'will talk', 'will talk'],
            ['would talk', 'would talk', 'would talk', 'would talk', 'would talk', 'would talk'],
            ['talk', 'talk', 'talk', 'talk', 'talk', 'talk'],
            ['have talked', 'have talked', 'has talked', 'have talked', 'have talked', 'have talked'],
            ['had talked', 'had talked', 'had talked', 'had talked', 'had talked', 'had talked'],
            ['will have talked', 'will have talked', 'will have talked', 'will have talked', 'will have talked', 'will have talked'],
            ['would have talked', 'would have talked', 'would have talked', 'would have talked', 'would have talked', 'would have talked'],
            ['talked', 'talked', 'talked', 'talked', 'talked', 'talked'],
            ]

list_to_wait = [
            ['wait', 'wait', 'waits', 'wait', 'wait', 'wait'],
            ['waited', 'waited', 'waited', 'waited', 'waited', 'waited'],
            ['will wait', 'will wait', 'will wait', 'will wait', 'will wait', 'will wait'],
            ['would wait', 'would wait', 'would wait', 'would wait', 'would wait', 'would wait'],
            ['wait', 'wait', 'wait', 'wait', 'wait', 'wait'],
            ['have waited', 'have waited', 'has waited', 'have waited', 'have waited', 'have waited'],
            ['had waited', 'had waited', 'had waited', 'had waited', 'had waited', 'had waited'],
            ['will have waited', 'will have waited', 'will have waited', 'will have waited', 'will have waited', 'will have waited'],
            ['would have waited', 'would have waited', 'would have waited', 'would have waited', 'would have waited', 'would have waited'],
            ['waited', 'waited', 'waited', 'waited', 'waited', 'waited'],
            ]

list_to_choose = [
            ['choose', 'choose', 'chooses', 'choose', 'choose', 'choose'],
            ['chose', 'chose', 'chose', 'chose', 'chose', 'chose'],
            ['will choose', 'will choose', 'will choose', 'will choose', 'will choose', 'will choose'],
            ['would choose', 'would choose', 'would choose', 'would choose', 'would choose', 'would choose'],
            ['choose', 'choose', 'chooses', 'choose', 'choose', 'choose'],
            ['have chosen', 'have chosen', 'has chosen', 'have chosen', 'have chosen', 'have chosen'],
            ['had chosen', 'had chosen', 'had chosen', 'had chosen', 'had chosen', 'had chosen'],
            ['will have chosen', 'will have chosen', 'will have chosen', 'will have chosen', 'will have chosen', 'will have chosen'],
            ['would have chosen', 'would have chosen', 'would have chosen', 'would have chosen', 'would have chosen', 'would have chosen'],
            ['chose', 'chose', 'chose', 'chose', 'chose', 'chose'],
            ]

list_to_go = [
            ['go', 'go', 'goes', 'go', 'go', 'go'],
            ['went', 'went', 'went', 'went', 'went', 'went'],
            ['will go', 'will go', 'will go', 'will go', 'will go', 'will go'],
            ['would go', 'would go', 'would go', 'would go', 'would go', 'would go'],
            ['go', 'go', 'goes', 'go', 'go', 'go'],
            ['have gone', 'have gone', 'has gone', 'have gone', 'have gone', 'have gone'],
            ['had gone', 'had gone', 'had gone', 'had gone', 'had gone', 'had gone'],
            ['will have gone', 'will have gone', 'will have gone', 'will have gone', 'will have gone', 'will have gone'],
            ['would have gone', 'would have gone', 'would have gone', 'would have gone', 'would have gone', 'would have gone'],
            ['went', 'went', 'went', 'went', 'went', 'went'],
            ]

list_to_descend = [
            ['descend', 'descend', 'descends', 'descend', 'descend', 'descend'],
            ['descended', 'descended', 'descended', 'descended', 'descended', 'descended'],
            ['will descend', 'will descend', 'will descend', 'will descend', 'will descend', 'will descend'],
            ['would descend', 'would descend', 'would descend', 'would descend', 'would descend', 'would descend'],
            ['descend', 'descend', 'descend', 'descend', 'descend', 'descend'],
            ['have descended', 'have descended', 'has descended', 'have descended', 'have descended', 'have descended'],
            ['had descended', 'had descended', 'had descended', 'had descended', 'had descended', 'had descended'],
            ['will have descended', 'will have descended', 'will have descended', 'will have descended', 'will have descended', 'will have descended'],
            ['would have descended', 'would have descended', 'would have descended', 'would have descended', 'would have descended', 'would have descended'],
            ['descended', 'descended', 'descended', 'descended', 'descended', 'descended'],
            ]

list_to_come = [
            ['come', 'come', 'comes', 'come', 'come', 'come'],
            ['came', 'came', 'came', 'came', 'came', 'came'],
            ['will come', 'will come', 'will come', 'will come', 'will come', 'will come'],
            ['would come', 'would come', 'would come', 'would come', 'would come', 'would come'],
            ['come', 'come', 'come', 'come', 'come', 'come'],
            ['have come', 'have come', 'has come', 'have come', 'have come', 'have come'],
            ['had come', 'had come', 'had come', 'had come', 'had come', 'had come'],
            ['will have come', 'will have come', 'will have come', 'will have come', 'will have come', 'will have come'],
            ['would have come', 'would have come', 'would have come', 'would have come', 'would have come', 'would have come'],
            ['came', 'came', 'came', 'came', 'came', 'came'],
            ]


# Smaller lists and dicts ----------------------------------------------------

dict_verbs_fr = {'etre' : dict_etre,
              'avoir' : dict_avoir,
              'parler' : dict_parler,
              'attendre' : dict_attendre,
              'choisir' : dict_choisir,
              'aller' : dict_aller,
              'descendre' : dict_descendre,
              'venir' : dict_venir
              }

dict_verbs_eng = {'to be' : dict_to_be,
              'to have' : dict_to_have,
              'to talk' : dict_to_talk,
              'to wait' : dict_to_wait,
              'to choose' : dict_to_choose,
              'to go' : dict_to_go,
              'to descend' : dict_to_descend,
              'to come' : dict_to_come
              }

list_verbs_fr = ['etre',
              'avoir',
              'parler',
              'attendre',
              'choisir',
              'aller',
              'descendre',
              'venir'
              ]

dict_verbs_fr_to_eng = {'etre' : 'to be',
              'avoir' : 'to have',
              'parler' : 'to talk',
              'attendre' : 'to wait',
              'choisir' : 'to choose',
              'aller' : 'to go',
              'descendre' : 'to descend',
              'venir' : 'to come'
             }
             

list_tenses = ['present' ,
             'imperfect' ,
             'future' ,
             'conditional' ,
             'subjunctive' ,
             'passe compose' ,
             'past perfect' ,
             'future perfect',
             'past conditional',
             'past subjunctive'
             ]

list_person_fr = ['je',
              'tu',
              'il',
              'nous',
              'vous',
              'ils'
              ]

list_person_eng = ['I',
              'you',
              'he',
              'we',
              'you',
              'they'
              ]

dict_person_fr_to_eng = {'je' : 'I',
              'tu' : 'you',
              'il' : 'he',
              'nous' : 'we',
              'vous' : 'you',
              'ils' : 'they'
              }


# temporarily disabled, play onely and no translate
# translate not yet fully functional (only works for be/etre)
"""
play_or_translate = input('Press P to Play or T to Translate: ')
"""

play_or_translate = 'p'

if play_or_translate == 'p' or play_or_translate == 'P':
        
    verb_fr = random.choice(list_verbs_fr)
    verb_eng = dict_verbs_fr_to_eng[verb_fr]
    person_fr = random.choice(list_person_fr)
    person_eng = dict_person_fr_to_eng[person_fr]
    tense = random.choice(list_tenses)
    
    answer_fr = f'{person_fr} {dict_verbs_fr[verb_fr][tense][person_fr]}'
    answer_fr = answer_fr.replace('je a', 'j\'a').replace('je e', 'j\'e').replace('je é', 'j\'é').replace('je i', 'j\'i').replace('je o', 'j\'o')
    answer_fr_plain = answer_fr.replace('â', 'a').replace('é', 'e').replace('ê', 'e').replace('û', 'u')
    
    answer_eng = f'{person_eng} {dict_verbs_eng[verb_eng][tense][person_eng]}'
    answer_eng_lower_i = answer_eng.replace('I', 'i')
    list_lang_choice = ['fr', 'en']
    
    answer_lang = random.choice(list_lang_choice)

    if answer_lang == 'fr':
        
        if tense == 'subjunctive' or tense == 'past subjunctive':
            print(f'\n({tense} tense)')
        else:
            pass
            
        if person_fr == 'vous':
            print('\n(\'you\' plural)')
        else:
            pass
        
        user_answer_fr = input(f'Say \'{answer_eng}\' in French [Enter \'H\' for hint]: ')  
            
        if user_answer_fr == 'H' or user_answer_fr == 'h':    
            
            if person_fr == 'vous':
                user_answer_fr = input(f'{tense.title()} tense. Say \'{answer_eng}\' in French (you plural): ')
            else:
                user_answer_fr = input(f'{tense.title()} tense. Say \'{answer_eng}\' in French: ')
            
            if user_answer_fr == answer_fr:
                print(f'Nice. \'{answer_eng}\' in French is \'{answer_fr}\'')
                answers_correct = correct_answer_count_add_one()
                answers_total = total_answer_count()
                
            else:
                if user_answer_fr == answer_fr_plain:
                    print(f'Nice, but watch the accents. \'{answer_eng}\' in French is \'{answer_fr}\'')
                    answers_correct = correct_answer_count_add_one()
                    answers_total = total_answer_count()
                else:
                    print(f'Close, but not correct. \'{answer_eng}\' in French is \'{answer_fr}\'')
                    answers_correct = correct_answer_count_add_zero()
                    answers_total = total_answer_count()
                
        else:
           
            if user_answer_fr == answer_fr:
                print(f'Nice. \'{answer_eng}\' in French is \'{answer_fr}\'')
                answers_correct = correct_answer_count_add_one()
                answers_total = total_answer_count()
                
            else:
                if user_answer_fr == answer_fr_plain:
                    print(f'Nice, but watch the accents. \'{answer_eng}\' in French is \'{answer_fr}\'')
                    answers_correct = correct_answer_count_add_one()
                    answers_total = total_answer_count()
                else:
                    print(f'Close, but not correct. \'{answer_eng}\' in French is \'{answer_fr}\'')
                    answers_correct = correct_answer_count_add_zero()
                    answers_total = total_answer_count()
                    
    else:
        
        if tense == 'subjunctive' or tense == 'past subjunctive':
            print(f'\n({tense} tense)')
        else:
            pass
        
        user_answer_eng = input(f'Say \'{answer_fr}\' in English [Enter \'H\' for hint]: ')
        
        if user_answer_eng == 'H' or user_answer_eng == 'h': 
            
            user_answer_eng = input(f'{tense.title()} tense. Say \'{answer_fr}\' in English: ')
            
            if user_answer_eng == answer_eng or user_answer_eng == answer_eng_lower_i:
                print(f'Nice. \'{answer_fr}\' in English is \'{answer_eng}\'')
                answers_correct = correct_answer_count_add_one()
                answers_total = total_answer_count()
                
            else:
                print(f'Close, but not correct. \'{answer_fr}\' in French is \'{answer_eng}\'')
                answers_correct = correct_answer_count_add_zero()
                answers_total = total_answer_count()
        else:
            
            if user_answer_eng == answer_eng or user_answer_eng == answer_eng_lower_i:
                print(f'Nice. \'{answer_fr}\' in English is \'{answer_eng}\'')
                answers_correct = correct_answer_count_add_one()
                answers_total = total_answer_count()
                
            else:
                print(f'Close, but not correct. \'{answer_fr}\' in French is \'{answer_eng}\'')
                answers_correct = correct_answer_count_add_zero()
                answers_total = total_answer_count()
                
    print(f'{answers_correct} answers of {answers_total} correct '
          f'({int(round(answers_correct/answers_total * 100, 0))}%)')

elif play_or_translate == 't' or play_or_translate == 'T':
    
    user_phrase = input('Choose a phrase to translate: ')
    
    phrase_person = user_phrase.split()[0]
    phrase_verb = ' '.join(user_phrase.split()[1:])
    
    lang_check = [1 if i == phrase_person else 0 for i in list_person_fr]
    
    if sum(lang_check) > 0:
        
        phrase_lang = 'fr'
        
    else:
        phrase_lang = 'en'
        
    if phrase_lang == 'fr':
        
        phrase_person_position = list_person_fr.index(phrase_person)
        phrase_verb_position = [i for i, sublist in enumerate(list_etre) 
                                if phrase_verb in sublist][0]
        
        translation_person = list_person_eng[phrase_person_position]
        translation_verb = list_to_be[phrase_verb_position][phrase_person_position]
        
        translation_phrase = f'{translation_person} {translation_verb}'
    
        print(f'\'{user_phrase}\' in English is \'{translation_phrase}\'')
        
    else:
        phrase_person_position = list_person_eng.index(phrase_person)
        phrase_verb_position = [i for i, sublist in enumerate(list_to_be) 
                                if phrase_verb in sublist][0]
        
        translation_person = list_person_fr[phrase_person_position]
        translation_verb = list_etre[phrase_verb_position][phrase_person_position]
        
        translation_phrase = f'{translation_person} {translation_verb}'
        
        print(f'\'{user_phrase}\' in French is \'{translation_phrase}\'')
    
    
        
    
        
    
    


