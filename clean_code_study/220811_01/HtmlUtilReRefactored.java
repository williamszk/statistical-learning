public class HtmlUtilReRefactored {
    public static String renderPageWithSetupsAndTeardowns(
            PageData pageData, boolean isSuite) throws Exception {
        if (isTestPage(pageData))
            includeSetupAndTeardownPages(pageData, isSuite);
        return pageData.getHtml();
    }
}
