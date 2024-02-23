def main():
    """
    ##################################################
    Comlete your code here
    Use m_perc and f_perc for your results
    ##################################################
    """
    maleS = int(input("Males in class: "))
    femaleS = int(input("Females in class: "))
    sum = int (maleS + femaleS)
    total = int (sum)
    m_perc = float ((maleS / sum) * 100)
    f_perc = float ((femaleS / sum) * 100)

    print ("The total amount of students is: ", total)
    print ('The percentage of males is',int(round(m_perc)),'%')
    print ('The percentage of females is',int(round(f_perc)),'%')
    """
    ########################################
    # Do not delete the return statement
    ########################################
    """
    return m_perc, f_perc


if __name__ == '__main__':
    main()
