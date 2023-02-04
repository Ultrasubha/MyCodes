using System.Collections;
using UnityEngine;
using UnityEngine.UI;

public class StaticLevel1Intro : MonoBehaviour
{
    //Just a bunch of Co-routines here

    public Text tutorial;
    public GameObject tutorialPanel;
    public GameObject mazeBlocker;
    public GameObject pauseButton;
    public GameObject noDiamond;
    public GameObject rewardPanel;
    public RewardSystem reward;
    public Langkey lang;

    private bool levelLoaded = true;
    private bool initial;
    private bool middle;
    private bool final;

    private void Update()
    {
        if (!reward.BlackscreenActive && !noDiamond.activeInHierarchy && !rewardPanel.activeInHierarchy)
        {
            if (levelLoaded)
                StartCoroutine(levelLoadDelay());
            if (initial)
                StartCoroutine(initialDelay());
            if (middle)
                StartCoroutine(middleDelay());
            if (final)
                StartCoroutine(finalDelay());
        }
        if (reward.BlackscreenActive && tutorialPanel.activeInHierarchy)
            tutorialPanel.gameObject.SetActive(false);
    }

    private IEnumerator levelLoadDelay()
    {
        yield return new WaitForSeconds(1);
        pauseButton.gameObject.SetActive(false);
        tutorialPanel.gameObject.SetActive(true);
        levelLoaded = false;
        initial = true;
    }

    private IEnumerator initialDelay()
    {
        tutorial.text = lang.initialDelay();
        yield return new WaitForSeconds(4);
        initial = false;
        middle = true;
    }

    private IEnumerator middleDelay()
    {
        tutorial.text = lang.middleDelay();
        tutorial.color = Color.black;
        yield return new WaitForSeconds(3);
        middle = false;
        final = true;
    }

    private IEnumerator finalDelay()
    {
        tutorial.text = lang.finalDelay();
        tutorial.color = Color.blue;
        yield return new WaitForSeconds(3);
        tutorialPanel.gameObject.SetActive(false);
        Destroy(mazeBlocker);
        pauseButton.gameObject.SetActive(true);
        final = false;
    }
}